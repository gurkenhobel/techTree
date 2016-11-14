using System;
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Text;
using Gurkenhobel.TechTree.Enums;
using Gurkenhobel.TechTree.Upgrades;

namespace Gurkenhobel.TechTree.Components
{



    public class TechTree : MonoBehaviour
    {
        private List<IUpgrade> _upgrades = new List<IUpgrade>();

        public string saveLocation;

        public List<IUpgrade> GetUpgrades()
        {
            return _upgrades;
        }

        public void AddUpgrade(string id)
        {
            IUpgrade newUpgrade;
            switch (id)
            {
                case "hp5":
                    newUpgrade = new Hp5
                    {
                        Layer = UpgradeLayer.Base,
                        Name = "Hp5"
                    };
                    break;
                case "reg1":
                    newUpgrade = new Reg1
                    {
                        Layer = UpgradeLayer.Base,
                        Name = "Reg1"
                    };
                    break;
                case "crit10":
                    newUpgrade = new Crit10
                    {
                        Layer = UpgradeLayer.Base,
                        Name = "Crit10"
                    };
                    break;
                case "atkSpd0_5":
                    newUpgrade = new AtkSpd0_5
                    {
                        Layer = UpgradeLayer.Base,
                        Name = "AtkSpd0_5"
                    };
                    break;
                default:
                    newUpgrade = null;
                    Debug.Log("invalid Upgrade: " + id);
                    break;
            }
            if (newUpgrade != null)
                Debug.Log("Added upgrade: " + newUpgrade.Name);

            _upgrades.Add(newUpgrade);
        }

        public void ReadFromFile()
        {
            var upgradeCodes = new List<string>();

            try
            {
                string line;
                StreamReader theReader = new StreamReader(Directory.GetCurrentDirectory() + saveLocation,
                    Encoding.Default);

                using (theReader)
                {
                    do
                    {
                        line = theReader.ReadLine();

                        if (line != null)
                        {
                            upgradeCodes.Add(line);
                        }
                    } while (line != null);
                    theReader.Close();
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("{0}\n", e.Message);
                return;
            }
            _upgrades = new List<IUpgrade>();
            foreach (var code in upgradeCodes)
            {
                AddUpgrade(code);
            }
        }



        // Use this for initialization
        private void Awake()
        {
            ReadFromFile();
        }

        // Update is called once per frame
    }
}
