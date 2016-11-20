using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using Gurkenhobel.TechTree.Enums;

namespace Gurkenhobel.TechTree
{
    public class PlayerChar : Character
    {
        public List<IUpgrade> Upgrades;

        public void UpgradesChanged(List<IUpgrade> newUpgrades)
        {
            Upgrades = newUpgrades;
            ApplyUpgrades();
        }

        public void ApplyUpgrades()
        {
            var earlyLayer = Upgrades.Where(u => u.Layer == UpgradeLayer.Early);
            var baseLayer = Upgrades.Where(u => u.Layer == UpgradeLayer.Base);
            var lateLayer = Upgrades.Where(u => u.Layer == UpgradeLayer.Late);
            CharacterStats = _baseStats.Clone();

            foreach (var upgrade in earlyLayer)
            {
                upgrade.Apply(CharacterStats);
                //Debug.Log("applied upgrade: " + upgrade.Name);
            }
            foreach (var upgrade in baseLayer)
            {
                upgrade.Apply(CharacterStats);
                //Debug.Log("applied upgrade: " + upgrade.Name);
            }
            foreach (var upgrade in lateLayer)
            {
                upgrade.Apply(CharacterStats);
                //Debug.Log("applied upgrade: " + upgrade.Name);
            }
        }

    }
}
