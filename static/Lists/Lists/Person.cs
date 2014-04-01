using System;

namespace Lists
{
    class Person
    {
        public string Last  { get; set; }
        public string First { get; set; }
        public string Email { get; set; }
        public string Phone { get; set; }

        public string FullName { get { return string.Format("{0}, {1}", Last, First); } }

        public Person(string last, string first, string email, string phone)
        {
            Last = last;
            First = first;
            Email = email;
            Phone = phone;
        }

        public Person(string last, string first, string email)
            : this(last, first, email, "")
        {
        }

        public override string ToString()
        {
            return string.Format("{0} [{1}, {2}]", FullName, Email, Phone);
        }

        public int CompareTo(Person other)
        {
            return string.Compare(this.FullName, other.FullName, true);
        }
    }
}
