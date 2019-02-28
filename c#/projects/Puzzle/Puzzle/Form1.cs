using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Puzzle
{
    public partial class Form1 : Form
    {
        Random random = new Random();

        List<string> icons = new List<string>()
        {
            "p", "p", "y", "y", "t", "t", "h", "h",
            "o", "o", "n", "n", "3", "3", ".", "."
        };

        Label firstCliked, secondClicked;

        public Form1()
        {
            InitializeComponent();
            AssignIconsToSquares();
        }

        private void label_Click(object sender, EventArgs e)
        {
            if (firstCliked != null && secondClicked != null)
                return;

            Label click_Label = sender as Label;

            if (click_Label == null)
                return;
            if (click_Label.ForeColor == Color.Black)
                return;
            if (firstCliked == null)
            {
                firstCliked = click_Label;
                firstCliked.ForeColor = Color.Black;
                return;
            }

            secondClicked = click_Label;
            secondClicked.ForeColor = Color.Black;

            CheckForWinner();

            if (firstCliked.Text == secondClicked.Text)
            {
                firstCliked = null;
                secondClicked = null;
            }
            else
                timer1.Start();
        }
        private void CheckForWinner()
        {
            Label label;
            for (int i = 0; i < tableLayoutPanel1.Controls.Count; i++)
            {
                label = tableLayoutPanel1.Controls[i] as Label;
                if (label != null && label.ForeColor == label.BackColor)
                    return;
            }
            MessageBox.Show("You have a W0N");
            Close();
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            timer1.Stop();

            firstCliked.ForeColor = firstCliked.BackColor;
            secondClicked.ForeColor = secondClicked.BackColor;
            firstCliked = null;
            secondClicked = null;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void AssignIconsToSquares()
        {
            Label label;
            int randomNumber;
            for (int i = 0; i < tableLayoutPanel1.Controls.Count; i++)
            {
                if (tableLayoutPanel1.Controls[i] is Label)
                    label = (Label)tableLayoutPanel1.Controls[i];
                else
                    continue;

                randomNumber = random.Next(0, icons.Count);
                label.Text = icons[randomNumber];

                icons.RemoveAt(randomNumber);
            }
        }
    }
}