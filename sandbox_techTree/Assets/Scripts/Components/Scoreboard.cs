using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class Scoreboard : MonoBehaviour
{
    public Text LevelText;

    private int _level = 0;

    public int Level
    {
        get
        {
            return _level;
        }

        set
        {
            _level = value;
        }
    }

    // Use this for initialization
    void Start()
    {

    }

    
    void Update()
    {
        LevelText.text = "Opponent # " + Level;
    }
}
