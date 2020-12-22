
import time
import serial

def ByteToHex( bins ):
    return ''.join( [ "%02X" % x for x in bins ] ).strip()

def HexToAscii(src):
    res = ''
    for x in range(0, len(src), 2):
      res += (chr(int(src[x: x+2],16)))
    return res.strip()

def ResultToDouble( srcBytes ):
    if len(srcBytes) > 3:
       return ''.join(chr(x) for x in srcBytes[3:-1]).strip()
    return ''
    
if __name__ == '__main__':
    s = serial.Serial(
        port='COM4',
        baudrate=9600,
        timeout=1
        #parity= serial.PARITY_MARK,
        #stopbits=serial.STOPBITS_ONE
        #bytesize=serial.SEVENBITS
    )  
    
    while True:
        count = s.inWaiting()
        if count > 0 :
            time.sleep(0.05)
            count = s.inWaiting()
            f = open('data.txt', 'a')
            res = s.read(count)
            data = ResultToDouble(res)
            f.writelines( '\n' + time.ctime(time.time())+'  '+ str(data) + ' m')
            if 'ERR--' in data :
                continue
            print(str(data) + ' m')
            data = round(float(data)*100,3)
            ByteToHex(res)
            f.writelines( '\n' + time.ctime(time.time())+'  '+ str(data) + ' cm')
            print(str(data) + ' cm')
            f.close()
            time.sleep(0.1)
                        
         
