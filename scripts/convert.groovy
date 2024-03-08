import org.jlab.io.base.DataBank;
import org.jlab.io.base.DataEvent;
import org.jlab.io.hipo.HipoDataSource;

s = ""
HipoDataSource reader = new HipoDataSource();
reader.open(args[0])
i = 0
while(reader.hasEvent()){
    if (i%10000==0) println (i)
    DataEvent event = reader.getNextEvent();
    if (event.hasBank("rec::event")){
        if (s)  s = s + "," + i
        else s = s + i

    }
    i++
}
// print(s)
// println(args)
def myFile = new File(args[1])
myFile.write(s)
