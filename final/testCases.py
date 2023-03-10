"""
    Name: TestCases.py
    Created: 1/28/2023
    Author: Katherine Smirnov

    Test Cases for gradeDataParser.py and WebScraper.py

"""


import unittest
import parser

class TestStringMethods(unittest.TestCase):

    def testParserAllprovided(self):
        """ testParserAllprovided()
                Tests parseGradeData() will all 3 parameters
        """

        returnVal = [{'TERM_DESC': 'Fall 2013', 'aprec': '20.0', 'bprec': '28.0', 'cprec': '32.0', 'crn': '14528', 'dprec': '4.0',
          'fprec': '16.0', 'instructor': 'Arbo, Matthew David'},
         {'TERM_DESC': 'Spring 2014', 'aprec': '26.7', 'bprec': '13.3', 'cprec': '33.3', 'crn': '36118',
          'dprec': '20.0', 'fprec': '6.7', 'instructor': 'Arbo, Matthew David'}]

        assert parser.parseGradeData("MATH", "111", "Arbo, Matthew David") == returnVal


    def testParser2provided(self):
        """ testParser2provided()
                    Tests parseGradeData() will class name
        """

        returnVal = {'TERM_DESC': 'Spring 2014', 'aprec': '38.9', 'bprec': '19.4', 'cprec': '22.2', 'crn': '38531', 'dprec': '11.1', 'fprec': '8.3', 'instructor': 'Sinclair, Christopher Dean'}, {'TERM_DESC': 'Spring 2015', 'aprec': '25.0', 'bprec': '29.5', 'cprec': '29.5', 'crn': '33691', 'dprec': '6.8', 'fprec': '9.1', 'instructor': 'Pazdan-Siudeja, Liliana Anna'}, {'TERM_DESC': 'Spring 2016', 'aprec': '29.5', 'bprec': '36.4', 'cprec': '22.7', 'crn': '33652', 'dprec': '9.1', 'fprec': '2.3', 'instructor': 'Pazdan-Siudeja, Liliana Anna'}
        assert parser.parseGradeData("MATH", "343", "") == returnVal


    def testWebScraper(self):
        """ testWebScraper()
                Verifies 'Faculty.js' holds the correct names from the Wayback Machine, and are correctly formatted without
                    middle name.
        """
        #what the names would be from the wayback machine
        returnVal = {
            "BI": [
                "Barkan, Alice",
                "Bohannan, Brendan",
                "Bowerman, Bruce",
                "Bradshaw, William",
                "Bridgham, Scott",
                "Carrier, Mark",
                "Conery, John",
                "Cresko, William",
                "Dickman, Alan",
                "Doe, Chris",
                "Eisen, Judith",
                "Emlet, Richard",
                "Green, Jessica",
                "Guillemin, Karen",
                "Herman, Victoria",
                "Hodder, Janet",
                "Hulslander, Cristin",
                "Johnson, Eric",
                "Kelly, Alan",
                "Lockery, Shawn",
                "Lombardi, Patteson",
                "Maslakova, Svetlana",
                "Neill, Cristopher",
                "O\u2019Day, Peter",
                "Phillips, Patrick",
                "Postlethwait, John",
                "Roberts, William",
                "Roy, Bitty",
                "Schlenoff, Debbie",
                "Selker, Eric",
                "Selker, Jeanne",
                "Shanks, Alan",
                "Sprague, George",
                "Sprague, Karen",
                "Stankunas, Kryn",
                "Stiefbold, Carl",
                "Streisfeld, Matthew",
                "Takahashi, Terry",
                "Thornton, Joseph",
                "Tublitz, Nathan",
                "Washbourne, Philip",
                "Weeks, Janis",
                "Westerfield, Monte",
                "Wetherwax, Peter",
                "Wood, Michelle",
                "Young, Craig",
                "Zong, Hui",
                "Rumrill, Steven",
                "Wagner, David",
                "Bajer, Andrew",
                "Bonnett, Howard",
                "Capaldi, Roderick",
                "Carroll, George",
                "Castenholz, Richard",
                "Kimmel, Charles",
                "Munz, Frederick",
                "Rudy, Paul",
                "Schabtach, Eric",
                "Shapiro, Lynda",
                "Stahl, Franklin",
                "Terwilliger, Nora",
                "Udovic, Daniel",
                "Wessells, Norman",
                "Weston, James",
                "Wisner, Herbert"
            ],
            "CH": [
                "Berglund, Andy",
                "Boettcher, Shannon",
                "Cina, Jeffrey",
                "De Rose, Victoria",
                "Doxsee, Kenneth",
                "Engelking, Paul",
                "Exton, Deborah",
                "Guenza, Marina",
                "Haack, Julie",
                "Haley, Michael",
                "Hawley, Diane",
                "Hutchison, James",
                "Johnson, Darren",
                "Johnson, David",
                "Kellman, Michael",
                "Koscho, Michael",
                "Lonergan, Mark",
                "Marcus, Andrew",
                "Nazin, George",
                "Nolen, Brad",
                "Page, Catherine",
                "Pluth, Michael",
                "Prehoda, Kenneth",
                "Richmond, Geraldine",
                "Stevens, Tom",
                "Sullivan, David",
                "Tyler, David",
                "Williams, Gregory",
                "Hardwick, John",
                "Barnhard, Ralph",
                "Branchaud, Bruce",
                "Dahlquist, Frederick",
                "Dyke, Thomas",
                "Griffith, Hayes",
                "Herrick, David",
                "Keana, John",
                "Long, James",
                "Mazo, Robert",
                "Schellman, John",
                "von Hippel, Peter",
                "Wolfe, Raymond"
            ],
            "CIS": [
                "Ariola, Zena",
                "Childs, Hank",
                "Dou, Dejing",
                "Faulk, Stuart",
                "Fickas, Stephen",
                "Freeman Hennessy, Kathleen",
                "Hennessy, Michael",
                "Hornof, Anthony",
                "Kinsy, Michel",
                "Li, Jun",
                "Lowd, Daniel",
                "Malony, Allen",
                "Norris, Boyana",
                "Proskurowski, Andrzej",
                "Rejaie, Reza",
                "Wills, Eric",
                "Wilson, Christopher",
                "Young, Michal",
                "Douglas, Sarah",
                "Farley, Arthur",
                "Lo, Virginia",
                "Luks, Eugene",
                "Stevens, Kent",
                "Conery, John",
                "Lobben, Amy",
                "Stolet, Jeffrey",
                "Thornton, Joseph",
                "Tucker, Don"
            ],
            "HPHY": [
                "Chou, Li-Shan",
                "Christie, Anita",
                "Dawson, Sierra",
                "Dreyer, Hans",
                "Gilbert, Jeffrey",
                "Golden, Grace",
                "Hahn, Michael",
                "Halliwill, John",
                "Karduna, Andrew",
                "Lovering, Andrew",
                "Minson, Christopher",
                "Runyeon, Jon",
                "Brandon, John",
                "Brown, Richard",
                "Chang, Chien-Chi",
                "Chesnutt, Mark",
                "Colasurdo, Michael",
                "Collis, Dennis",
                "Fish, Mathews",
                "Fitzpatrick, Daniel",
                "Gladstone, Igor",
                "Goodman, Randall",
                "Grall, Sarah",
                "Harding, Aaron",
                "Hawn, Jerold",
                "James, Stanley",
                "Jewett, Brian",
                "Jones, Donald",
                "Kaplan, Paul",
                "Katz, Vern",
                "Kosek, Peter",
                "Lantz, Brett",
                "Lau, Samuel",
                "Lin, Victor",
                "Melton, John",
                "Nichols, Brian",
                "Padgett, Richard",
                "Robertson, Rick",
                "Shumway-Cook, Anne",
                "Singer, Kenneth",
                "Terrell, Kimberly",
                "Bates, Barry",
                "Klug, Gary",
                "Osternig, Louis",
                "Troxel, Richard",
                "Woollacott, Marjorie"
            ],
            "MATH": [
                "Akhtari, Shabnam",
                "Berenstein, Arkadiy",
                "Botvinnik, Boris",
                "Bownik, Marcin",
                "Brundan, Jonathan",
                "Dugger, Daniel",
                "Gilkey, Peter",
                "Harker, Hayden",
                "He, Weiyong",
                "Hervert, Fred",
                "Isenberg, James",
                "Kleshchev, Alexander",
                "Levin, David",
                "Lin, Huaxin",
                "Lu, Peng",
                "Nganou, Jean",
                "Ostrik, Victor",
                "Phillips, Christopher",
                "Polishchuk, Alexander",
                "Price, Michael",
                "Proudfoot, Nicholas",
                "Sadofsky, Hal",
                "Shelton, Brad",
                "Sinclair, Christopher",
                "Sinha, Dev",
                "Siudeja, Bartlomiej",
                "Tingey, Craig",
                "Vaintrob, Arkady",
                "Vologodski, Vadim",
                "Wang, Hao",
                "Warren, Micah",
                "Xu, Yuan",
                "Young, Benjamin",
                "Yuzvinsky, Sergey",
                "Solovay, Robert",
                "Anderson, Frank",
                "Andrews, Fred",
                "Barnes, Bruce",
                "Barrar, Richard",
                "Beelman, Glenn",
                "Curtis, Charles",
                "Dyer, Micheal",
                "Freeman, Robert",
                "Kantor, William",
                "Koch, Richard",
                "Leahy, John",
                "Libeskind, Shlomo",
                "Palmer, Theodore",
                "Ross, Kenneth",
                "Seitz, Gary",
                "Sieradski, Allan",
                "Thomas, Stuart",
                "Truax, Donald",
                "Vitulli, Marie",
                "Walter, Marion",
                "Ward, Lewis",
                "Wolfe, Jerry",
                "Wright, Charles"
            ],
            "Neuroscience": [
                "Awh, Edward",
                "Dassonville, Paul",
                "Doe, Chris",
                "Eisen, Judith",
                "Kentros, Clifford",
                "Kimmel, Charles",
                "Lockery, Shawn",
                "Neville, Helen",
                "O\u2019Day, Peter",
                "Neill, Cristopher",
                "Postlethwait, John",
                "Roberts, William",
                "Takahashi, Terry",
                "Vogel, Edward",
                "Washbourne, Philip",
                "Weeks, Janis",
                "Wehr, Michael",
                "Westerfield, Monte",
                "Woollacott, Marjorie"
            ],
            "PHYS": [
                "Belitz, Dietrich",
                "Bothun, Gregory",
                "Brau, James",
                "Chang, Spencer",
                "Corwin, Eric",
                "Csonka, Paul",
                "Deshpande, Nilendra",
                "Deutsch, Miriam",
                "Donnelly, Russell",
                "Fisher, Scott",
                "Frey, Raymond",
                "Gregory, Stephen",
                "Haydock, Roger",
                "Hsu, Stephen",
                "Imamura, James",
                "Jenkins, Timothy",
                "Kevan, Stephen",
                "Kribs, Graham",
                "Livelybrooks, Dean",
                "Majewski, Stephanie",
                "Matthews, Brian",
                "McMorran, Benjamin",
                "Micklavzina, Stanley",
                "Nockel, Jens",
                "Parthasarathy, Raghuveer",
                "Raymer, Michael",
                "Remington, Stephen",
                "Schombert, James",
                "Soper, Davison",
                "Steck, Daniel",
                "Strom, David",
                "Taylor, Richard",
                "Toner, John",
                "Torrence, Eric",
                "van Enk, Steven",
                "Wang, Hailin",
                "Schofield, Robert",
                "Sinev, Nikolai",
                "Vignola, Frank",
                "Crasemann, Bernd",
                "Girardeau, Marvin",
                "Hwa, Rudolph",
                "Lefevre, Harlan",
                "McClure, Joel",
                "McDaniels, David",
                "Moseley, John",
                "Overley, Jack",
                "Park, Kwangjai",
                "Rayfield, George",
                "Sokoloff, David",
                "Zimmerman, Robert"
            ],
            "PSY": [
                "Ablow, Jennifer",
                "Allen, Nicholas",
                "Arrow, Holly",
                "Awh, Edward",
                "Baldwin, Dare",
                "Berkman, Elliot",
                "Dassonville, Paul",
                "Andrews Espy, Kimberly",
                "Fisher, Philip",
                "Freyd, Jennifer",
                "Nagayama Hall, Gordon",
                "Hodges, Sara",
                "Kentros, Clifford",
                "Laurent, Heidemarie",
                "Mauro, Robert",
                "Mayr, Ulrich",
                "Measelle, Jeffrey",
                "Mehta, Pranjal",
                "Moses, Louis",
                "Neville, Helen",
                "Pfeifer, Jennifer",
                "Saucier, Gerard",
                "Sereno, Margaret",
                "Shariff, Azim",
                "Slovic, Paul",
                "Srivastava, Sanjay",
                "Taylor, Marjorie",
                "Tucker, Don",
                "Unsworth, Nash",
                "Vogel, Edward",
                "Wehr, Michael",
                "Goldberg, Lewis",
                "Gordon-Lickey, Barbara",
                "Gordon-Lickey, Marvin",
                "Hintzman, Douglas",
                "Hyman, Ray",
                "Keutzer, Carolin",
                "Kimble, Daniel",
                "Lewinsohn, Peter",
                "Lichtenstein, Edward",
                "Littman, Richard",
                "Marrocco, Richard",
                "Posner, Michael",
                "Rothbart, Mary",
                "Rothbart, Myron",
                "Sundberg, Norman",
                "Weiss, Robert"
            ]
        }
        assert returnVal == parser.getFacultyData(None)


if __name__ == '__main__':
    unittest.main()