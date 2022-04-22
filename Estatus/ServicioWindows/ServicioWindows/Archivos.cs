using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Linq;
using System.ServiceProcess;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;
using System.IO;

namespace ServicioWindows
{
    partial class Archivos : ServiceBase
    {
        bool blBandera = false;
        public Archivos()
        {
            InitializeComponent();
        }

        protected override void OnStart(string[] args)
        {
            stLapso.Start();
        }

        protected override void OnStop()
        {
            stLapso.Stop();
        }

        private void stLapso_Elapsed(object sender, System.Timers.ElapsedEventArgs e)
        {
            if (blBandera) return;

            try
            {
                EventLog.WriteEntry("Se inicio proceso de copiado", EventLogEntryType.Information);
                string stRutaorigen = ConfigurationSettings.AppSettings["stRutaorigen"].ToString();
                string stRutadestino = ConfigurationSettings.AppSettings["stRutadestino"].ToString();
                DirectoryInfo di = new DirectoryInfo(stRutaorigen);

                foreach(var archivo in di.GetFiles("*",SearchOption.AllDirectories))
                {
                    if(File.Exists(stRutadestino + archivo.Name))
                    {
                        File.SetAttributes(stRutadestino + archivo.Name, FileAttributes.Normal);
                        File.Delete(stRutadestino + archivo.Name);  
                    }
                    File.Copy(stRutaorigen + archivo.Name, stRutadestino + archivo.Name);
                    File.SetAttributes(stRutadestino + archivo.Name, FileAttributes.Normal);

                    if (File.Exists(stRutadestino + archivo.Name))
                        EventLog.WriteEntry("Se copio el archivo con exito", EventLogEntryType.Information);
                    else
                        EventLog.WriteEntry("No se copio el archivo con exito", EventLogEntryType.Information);
                }
                EventLog.WriteEntry("Se finalizo el proceso de copiado", EventLogEntryType.Information);
            }
            catch (Exception ex)
            {
                EventLog.WriteEntry(ex.Message, EventLogEntryType.Error);
            }
            blBandera = false;
        }
    }
}
