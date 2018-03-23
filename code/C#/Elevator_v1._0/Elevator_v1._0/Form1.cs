using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Elevator_v1._0
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 엘레베이터 1
        public int doorstate = 0; // 문 상태 0:닫힘 1:열림
        public int directstate = 0; // 방향 0:정지 1:위로 2:아래로
        public int[] callfloor = new int[10] { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        public int mov = 5; // 문관련 움직이는 값
        public int dx = -1; // 문관련 이동값
        public int dy = 1; // 문관련 이동값
        private int ele1_floor = 1; //엘베1 현재 층수
        private int time = 0;

        private void On_button1_Click(object sender, EventArgs e)
        {
            timer4.Enabled = false;
            if (doorstate != 1)
            {
                timer1.Enabled = true;
            }
            if (timer2.Enabled == true)
            {
                time = 10 - time;
                timer2.Enabled = false;
                timer1.Enabled = true;
            }
        }
        private void On_button2_Click(object sender, EventArgs e)
        {
            if (doorstate != 0)
            {
                timer2.Enabled = true;
            }
        }

        private void On_timer1_Tick(object sender, EventArgs e)// 문열림
        {
            if (timer3.Enabled == true)
            {
                timer3.Enabled = false;
            }
            int x = pictureBox1.Location.X + mov * dx;
            int y = pictureBox2.Location.X + mov * dy;

            pictureBox1.Left = x;
            pictureBox2.Left = y;
            time += 1;
            timer4.Interval = 3000;
            timer4.Enabled = true;
            if (time == 10)
            {
                time = 0;
                doorstate = 1;
                timer1.Enabled = false;
            }
        }
        private void On_timer2_Tick(object sender, EventArgs e)// 문닫힘
        {
            int x = pictureBox1.Location.X + mov * -dx;
            int y = pictureBox2.Location.X + mov * -dy;

            pictureBox1.Left = x;
            pictureBox2.Left = y;
            time += 1;
            if (time == 10)
            {
                time = 0;
                doorstate = 0;
                timer2.Enabled = false;
            }
            if (directstate == 1 && callfloor[0] % 10 < ele1_floor && ele1_floor != 1)
            {
                timer5.Interval = 2000;
                timer5.Enabled = true;
            }
            else if (directstate == 2 && callfloor[0] % 10 > ele1_floor && ele1_floor != 5)
            {
                timer5.Interval = 2000;
                timer5.Enabled = true;
            }
            else
            {
                timer5.Interval = 1000;
                timer5.Enabled = true;
            }
        }
        private void On_timer3_Tick(object sender, EventArgs e)// 층수
        {
            if (callfloor[0] == 0) { }
            else if (ele1_floor < callfloor[0] % 10)
            {
                ele1_floor++;
            }
            else if (ele1_floor > callfloor[0] % 10)
            {
                ele1_floor--;
            }
            else
            {
                if (doorstate != 1)
                {
                    timer1.Enabled = true;
                }
                timer3.Enabled = false;
                switch (ele1_floor)
                {
                    case 1: checkBox1.Checked = false; checkBox11.Checked = false; break;
                    case 2:
                        checkBox2.Checked = false;
                        if (callfloor[0] == 12)
                        {
                            checkBox12.Checked = false;
                            if (directstate == 2)
                            {
                                directstate = 1;
                            }
                        }
                        else if (callfloor[0] == 22)
                        {
                            checkBox22.Checked = false;
                            if (directstate == 1)
                            {
                                directstate = 2;
                            }
                        }
                        break;

                    case 3:
                        checkBox3.Checked = false;
                        if (callfloor[0] == 13)
                        {
                            checkBox13.Checked = false;
                            if (directstate == 2)
                            {
                                directstate = 1;
                            }
                        }
                        else if (callfloor[0] == 23)
                        {
                            checkBox23.Checked = false;
                            if (directstate == 1)
                            {
                                directstate = 2;
                            }
                        }
                        break;

                    case 4:
                        checkBox4.Checked = false;
                        if (callfloor[0] == 14)
                        {
                            checkBox14.Checked = false;
                            if (directstate == 2)
                            {
                                directstate = 1;
                            }
                        }
                        else if (callfloor[0] == 24)
                        {
                            checkBox24.Checked = false;
                            if (directstate == 1)
                            {
                                directstate = 2;
                            }
                        }
                        break;

                    case 5: checkBox5.Checked = false; checkBox25.Checked = false; break;
                }
            }
            switch (ele1_floor)
            {
                case 1: textBox1.Text = "1"; break;
                case 2: textBox1.Text = "2"; break;
                case 3: textBox1.Text = "3"; break;
                case 4: textBox1.Text = "4"; break;
                case 5: textBox1.Text = "5"; break;
            }
        }
        private void On_timer4_Tick(object sender, EventArgs e)// 문열린후 닫히기
        {
            if (doorstate == 1)
            {
                timer2.Enabled = true;
            }
            timer4.Enabled = false;
        }
        private void On_timer5_Tick(object sender, EventArgs e)// 방향
        {
            if (callfloor[0] == 0)
            {
                directstate = 0;
                textBox3.Text = "-";
            }
            else if (callfloor[0] % 10 > ele1_floor)
            {
                directstate = 1;
                textBox3.Text = "U";
            }
            else if (callfloor[0] % 10 < ele1_floor)
            {
                directstate = 2;
                textBox3.Text = "D";
            }
            if (callfloor[0] != 0)
            {
                movestair();
                timer5.Enabled = false;
            }
        }

        private void lshift(int a)
        {
            for (int i = a; i < 9; i++)
            {
                if (callfloor[i] == 0)
                {
                    break;
                }
                else
                {
                    callfloor[i] = callfloor[i + 1];
                }
                callfloor[9] = 0;
            }
        }
        private void rshift(int a, int i)
        {
            for (int j = 9; j > 0; j--)
            {
                callfloor[j] = callfloor[j - 1];
            }
            callfloor[i] = a;
        }
        private void CreatCallfloor(int a)
        {
            for (int i = 0; i <= 9; i++)
            {
                if (a > 0 && a < 10)
                {
                    if (directstate == 1)
                    {
                        if (callfloor[i] > 0 && callfloor[i] < 10)
                        {
                            if (callfloor[i] % 10 > a % 10 && a % 10 > ele1_floor)
                            {
                                rshift(a, i);
                                break;
                            }
                        }
                        else if (callfloor[i] > 10 && callfloor[i] < 20)
                        {
                            if (callfloor[i] % 10 > a % 10 && a % 10 > ele1_floor)
                            {
                                rshift(a, i);
                                break;
                            }
                        }
                        else if (callfloor[i] > 20 && callfloor[i] < 30)
                        {
                            if (a % 10 > ele1_floor)
                            {
                                rshift(a, i);
                                break;
                            }
                        }
                        else if (callfloor[i] == 0)
                        {
                            callfloor[i] = a;
                            break;
                        }
                    }
                    else if (directstate == 2)
                    {
                        if (callfloor[i] > 0 && callfloor[i] < 10)
                        {
                            if (callfloor[i] % 10 < a % 10 && a % 10 < ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] > 10 && callfloor[i] < 20)
                        {
                            if (callfloor[i] % 10 < a % 10 && a % 10 < ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] > 20 && callfloor[i] < 30)
                        {
                            if (callfloor[i] % 10 < a % 10 && a % 10 < ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] == 0) { callfloor[i] = a; break; }
                    }
                    else { callfloor[i] = a; break; }
                }
                else if (a > 10 && a < 20)
                {
                    if (directstate == 1)
                    {
                        if (callfloor[i] > 0 && callfloor[i] < 10)
                        {
                            if (callfloor[i] % 10 > a % 10 && a % 10 > ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] > 10 && callfloor[i] < 20)
                        {
                            if (callfloor[i] % 10 > a % 10 && a % 10 > ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] > 20 && callfloor[i] < 30)
                        {
                            if (callfloor[i] % 10 > a % 10 && a % 10 > ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] == 0) { callfloor[i] = a; break; }
                    }
                    else if (directstate == 2)
                    {
                        if (callfloor[i] > 0 && callfloor[i] < 10)
                        {
                            if (callfloor[i] % 10 < a % 10 && a % 10 < ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] > 10 && callfloor[i] < 20)
                        {
                            if (callfloor[i] % 10 > a % 10) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] > 20 && callfloor[i] < 30)
                        {
                            if (callfloor[i] % 10 < a % 10 && a % 10 < ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] == 0) { callfloor[i] = a; break; }
                    }
                    else { callfloor[i] = a; break; }
                }
                else if (a > 20 && a < 30)
                {
                    if (directstate == 1)
                    {
                        if (callfloor[i] > 0 && callfloor[i] < 10)
                        {
                            if (a % 10 > ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] > 10 && callfloor[i] < 20)
                        {
                            if (a % 10 > ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] > 20 && callfloor[i] < 30)
                        {
                            if (a % 10 > callfloor[i] % 10) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] == 0) { callfloor[i] = a; break; }
                    }
                    else if (directstate == 2)
                    {
                        if (callfloor[i] > 0 && callfloor[i] < 10)
                        {
                            if (callfloor[i] % 10 < a % 10 && a % 10 > ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] > 10 && callfloor[i] < 20)
                        {
                            if (callfloor[i] % 10 < a % 10 && a % 10 < ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] > 20 && callfloor[i] < 30)
                        {
                            if (callfloor[i] % 10 < a % 10 && a % 10 < ele1_floor) { rshift(a, i); break; }
                        }
                        else if (callfloor[i] == 0) { callfloor[i] = a; break; }
                    }
                    else { callfloor[i] = a; break; }
                }
            }
            movestair();
        }
        private void DeleteCallfloor(int a)
        {
            if (a == 0)
            {
                lshift(a);
            }
            else
            {
                for (int i = 0; i < 10; i++)
                {
                    if (callfloor[i] == a)
                    {
                        lshift(i);
                        break;
                    }
                }
            }
            movestair();
        }
        private void movestair()
        {
            if (doorstate == 0)
            {
                if (callfloor[0] % 10 > ele1_floor)
                {
                    directstate = 1;
                }
                else if (callfloor[0] % 10 < ele1_floor)
                {
                    directstate = 2;
                }
                else if (callfloor[0] == 0)
                {
                    directstate = 0;
                }
                timer3.Interval = 1000;
                if (timer3.Enabled == false)
                {
                    timer3.Enabled = true;
                }
            }
        }


        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                if (ele1_floor == 1)
                {
                    checkBox1.Checked = false;
                }
                else { CreatCallfloor(1); }
            }
            else
            {
                DeleteCallfloor(1);
            }
        }
        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox2.Checked == true)
            {
                if (ele1_floor == 2)
                {
                    checkBox2.Checked = false;
                }
                else { CreatCallfloor(2); }
            }
            else { DeleteCallfloor(2); }
        }
        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox3.Checked == true)
            {
                if (ele1_floor == 3)
                {
                    checkBox3.Checked = false;
                }
                else { CreatCallfloor(3); }
            }
            else { DeleteCallfloor(3); }
        }
        private void checkBox4_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox4.Checked == true)
            {
                if (ele1_floor == 4)
                {
                    checkBox4.Checked = false;
                }
                else
                {
                    CreatCallfloor(4);
                }
            }
            else { DeleteCallfloor(4); }
        }
        private void checkBox5_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox5.Checked == true)
            {
                if (ele1_floor == 5)
                {
                    checkBox5.Checked = false;
                }
                else { CreatCallfloor(5); }
            }
            else { DeleteCallfloor(5); }
        }
        private void checkBox6_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox6.Checked == true)
            {
                textBox1.Text = "E";
                checkBox06.Checked = false;
                if (checkBox1.Checked == true || checkBox2.Checked == true || checkBox3.Checked == true || checkBox4.Checked == true || checkBox5.Checked == true)
                {
                    checkBox1.Checked = false;
                    checkBox2.Checked = false;
                    checkBox3.Checked = false;
                    checkBox4.Checked = false;
                    checkBox5.Checked = false;
                }
                if (doorstate != 1)
                {
                    for (int i = 0; i <= 4; i++)
                    {
                        int x = pictureBox1.Location.X + mov * -i;
                        int y = pictureBox2.Location.X + mov * i;

                        pictureBox1.Left = x;
                        pictureBox2.Left = y;
                    }
                }
            }
        }

        //외부버튼
        private void checkBox11_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox11.Checked == true)
            {
                if (ele1_floor == 1) { if (doorstate != 1) { timer1.Enabled = true; } checkBox11.Checked = false; }
                else { CreatCallfloor(11); }
            }
            else { DeleteCallfloor(11); }
        }
        private void checkBox12_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox12.Checked == true)
            {
                if (ele1_floor == 2 && directstate == 1) { if (doorstate != 1) { timer1.Enabled = true; } checkBox12.Checked = false; }
                else { CreatCallfloor(12); }
            }
            else { DeleteCallfloor(12); }
        }
        private void checkBox13_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox13.Checked == true)
            {
                if (ele1_floor == 3 && directstate == 1) { if (doorstate != 1) { timer1.Enabled = true; } checkBox13.Checked = false; }
                else { CreatCallfloor(13); }
            }
            else { DeleteCallfloor(13); }
        }
        private void checkBox14_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox14.Checked == true)
            {
                if (ele1_floor == 4 && directstate == 1) { if (doorstate != 1) { timer1.Enabled = true; } checkBox14.Checked = false; }
                else { CreatCallfloor(14); }
            }
            else { DeleteCallfloor(14); }
        }
        private void checkBox22_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox22.Checked == true)
            {
                if (ele1_floor == 2 && directstate == 2) { if (doorstate != 1) { timer1.Enabled = true; } checkBox22.Checked = false; }
                else { CreatCallfloor(22); }
            }
            else { DeleteCallfloor(22); }
        }
        private void checkBox23_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox23.Checked == true)
            {
                if (ele1_floor == 3 && directstate == 2) { if (doorstate != 1) { timer1.Enabled = true; } checkBox23.Checked = false; }
                else { CreatCallfloor(23); }
            }
            else { DeleteCallfloor(23); }
        }
        private void checkBox24_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox24.Checked == true)
            {
                if (ele1_floor == 4 && directstate == 2) { if (doorstate != 1) { timer1.Enabled = true; } checkBox24.Checked = false; }
                else { CreatCallfloor(24); }
            }
            else { DeleteCallfloor(24); }
        }
        private void checkBox25_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox25.Checked == true)
            {
                if (ele1_floor == 5) { if (doorstate != 1) { timer1.Enabled = true; } checkBox25.Checked = false; }
                else { CreatCallfloor(25); }
            }
            else { DeleteCallfloor(25); }
        }


        //엘리베이터2
        private void On_button3_Click(object sender, EventArgs e)
        {

        }
        private void On_button4_Click(object sender, EventArgs e)
        {

        }

        private void On_timer11_Tick(object sender, EventArgs e)
        {

        }
        private void On_timer12_Tick(object sender, EventArgs e)
        {

        }
        private void On_timer13_Tick(object sender, EventArgs e)
        {

        }
        private void On_timer14_Tick(object sender, EventArgs e)
        {

        }
        private void On_timer15_Tick(object sender, EventArgs e)
        {

        }
    }
}

