# non-GUI side: proceed normally, no need for special code

import time
while True:                          # non-GUI code
    print(time.asctime())            # sends to GUI process
    time.sleep(1.0)                  # no need to flush here
