require "faker"
require "uri"
require "net/http"

module Send
  class Sms
    def initialize(username, password, type: "non_emergency", count: 10, country: "en-US")
      @username = username
      @password = password
      @type = type
      @count = count

      Faker::Config.locale = country
    end

    def send_sms
      phone_numbers = []

      (1..@count).each { phone_numbers << Faker::PhoneNumber.cell_phone_in_e164 }

      if @type == "non_emergency"
        api = "http://localhost:3000/api/v1/sms_transactions/send_sms"
        message = "SEND DEMO MESSAGE WITH NON-EMERGENCY"
      else
        api = "http://localhost:3000/api/v1/sms_transactions/send_emergency_sms"
        message = "SEND DEMO MESSAGE WITH EMERGENCY"
      end

      uri = URI(api)
      request_body = {
        "message_type": @type,
        "message": message,
        "reference_id": "123",
        "demo": true,
        "phone_numbers[]": phone_numbers
      }

      request = Net::HTTP::Post.new(uri)
      request.basic_auth(@username, @password)
      request.set_form_data(request_body)

      response = Net::HTTP.start(uri.hostname, uri.port) do |http|
        http.request(request)
      end

      puts response.body
    end
  end
end

username = "444444c718d6adea93061121cf44d8293467fe04ce2300c131407f01a27489de1879e299262e122a7988169c9697267420faf4ac296f541fb29a2b939c8c510b"
secret = "c1945ba70ef8a7453b0f94b42fb27644e60d4634dc5245dae18c0251e128bf0c96a46ef2"

handler = Send::Sms.new(username, secret, count: 5)
handler.send_sms

