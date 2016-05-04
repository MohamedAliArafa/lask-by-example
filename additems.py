# # coding=utf-8
import models
#
from app import db
#
#
# # Bind the engine to the metadata of the Base class so that the
# # declaratives can be accessed through a DBdb.session instance
#
# # A DBdb.session() instance establishes all conversations with the database
# # and represents a "staging zone" for all the objects loaded into the
# # database db.session object. Any change made against the objects in the
# # db.session won't be persisted into the database until you call
# # db.session.commit(). If you're not happy about the changes, you can
# # revert all of them back to the last commit by calling
# # db.session.rollback()
#
#
# Cat1 = models.Category(name="Clothing")
# db.session.add(Cat1)
# db.session.commit()
# Cat2 = models.Category(name="Crafts")
# db.session.add(Cat2)
# db.session.commit()
# Cat3 = models.Category(name="Home")
# db.session.add(Cat3)
# db.session.commit()
# Cat4 = models.Category(name="Accessory")
# db.session.add(Cat4)
# db.session.commit()
# Cat5 = models.Category(name="Artwork")
# db.session.add(Cat5)
# db.session.commit()
#
# SubCat1 = models.SubCategory(name="Crocheting", category=Cat1)
# db.session.add(SubCat1)
# db.session.commit()
# SubCat2 = models.SubCategory(name="Children", category=Cat1)
# db.session.add(SubCat2)
# db.session.commit()
# SubCat3 = models.SubCategory(name="Knitting", category=Cat1)
# db.session.add(SubCat3)
# db.session.commit()
#
# SubCat4 = models.SubCategory(name="Floral Craft", category=Cat2)
# db.session.add(SubCat4)
# db.session.commit()
# SubCat5 = models.SubCategory(name="Woodworking", category=Cat2)
# db.session.add(SubCat5)
# db.session.commit()
# SubCat6 = models.SubCategory(name="Leathercraft", category=Cat2)
# db.session.add(SubCat6)
# db.session.commit()
#
# SubCat7 = models.SubCategory(name="Decor", category=Cat3)
# db.session.add(SubCat7)
# db.session.commit()
# SubCat8 = models.SubCategory(name="Lighting", category=Cat3)
# db.session.add(SubCat8)
# db.session.commit()
# SubCat9 = models.SubCategory(name="kitchen", category=Cat3)
# db.session.add(SubCat9)
# db.session.commit()
#
# SubCat11 = models.SubCategory(name="Rings", category=Cat4)
# db.session.add(SubCat11)
# db.session.commit()
# db.session.commit()
# SubCat13 = models.SubCategory(name="Earrings", category=Cat4)
# db.session.add(SubCat13)
# SubCat12 = models.SubCategory(name="Necklaces", category=Cat4)
# db.session.add(SubCat12)
# db.session.commit()
# SubCat14 = models.SubCategory(name="Bracelets", category=Cat4)
# db.session.add(SubCat14)
# db.session.commit()
#
# SubCat15 = models.SubCategory(name="Drawing", category=Cat5)
# db.session.add(SubCat15)
# db.session.commit()
# SubCat16 = models.SubCategory(name="Glass Art", category=Cat5)
# db.session.add(SubCat16)
# db.session.commit()
# SubCat17 = models.SubCategory(name="Photography", category=Cat5)
# db.session.add(SubCat17)
# db.session.commit()
#
# print "categories added"
#
User1 = models.User(name="Mohamed Arafa", email="arafa@gmail.com", mobile="0122222222", password="arafa2012")
db.session.add(User1)
db.session.commit()

User2 = models.User(name="Nezar Saleh", email="nezar@gmail.com", mobile="0122222222", password="nezar123")
db.session.add(User2)
db.session.commit()

User3 = models.User(name="Nora Amer", email="nora@gmail.com.com", mobile="0122222222", password="nora123")
db.session.add(User3)
db.session.commit()

User4 = models.User(name="Ebrahim Arafa", email="hema@gameil.com", mobile="0122222222", password="hema123")
db.session.add(User4)
db.session.commit()

User5 = models.User(name="Ahmed El-Mahalawy", email="ahmed@gmail.com", mobile="0122222222", password="ahmed123")
db.session.add(User1)
db.session.commit()

User6 = models.User(name="Ehab Hashem", email="ehab@gmail.com", mobile="0122222222", password="ehab123")
db.session.add(User2)
db.session.commit()

User7 = models.User(name="Eslam Abo El-Fotoh", email="eslam@gmail.com.com", mobile="0122222222", password="eslam123")
db.session.add(User3)
db.session.commit()

User8 = models.User(name="Ahmed Maher", email="maher@gameil.com", mobile="0122222222", password="maher123")
db.session.add(User4)
db.session.commit()

User9 = models.User(name="Mohamed El-Gazzar", email="gazzar@gameil.com", mobile="0122222222", password="gazzar123")
db.session.add(User4)
db.session.commit()
# # Menu for UrbanBurger
# Shop1 = models.Shop(shop_name="Barnes & Noble", owner_name="Mohamed Arafa", owner_email="arafa@gmail.com",
#                             mobile="0122222222", password="arafa2012", shop_profile_pic="570269c0f2302.png",
#                             shop_cover_pic="570269c0f2302.png", description="Barnes & Noble, Inc., is a Fortune 500 company, the largest retail bookseller in the United"
#                                         " States, and a leading retailer of content, digital media and educational products "
#                                         "in the country.")
#
# db.session.add(Shop1)
# db.session.commit()
#
# Items2 = models.Items(name="Awesome Monster Hat", image="56fd78def1754.jpg",
#                               description="This monster hat will draw comments from everyone who sees it! It can be made in any color"
#                                           " and any size! Just put color and size on the message to seller section! Come on! You know"
#                                           " you want a monster hat! ",
#                               quantity=10, price="3.49", short_description="Entree", SubCategory=SubCat1, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
# Items1 = models.Items(name="SOFT CLOTH DOLLS BLUES", image="56fd6be50af78.jpg",
#                               description="YOU ARE BUYING A SET OF DOLLS WITH ALL NATURAL BOTH ARE FILLED WITH POLY FILL AND ALL "
#                                           "NEW MATERIAL THE LOOK IS THAT OF AND OLD CHURCH DOLL THAT MEANS ITS DOES NOT MAKE NOICE"
#                                           " AND KIDS ARE THROW IT LOL AND CHEW ON IT AND THEN IT CAN BE WASHED ",
#                               quantity=10, price="2.99", short_description="Appetizer", SubCategory=SubCat1, shop=Shop1)
#
# db.session.add(Items1)
# db.session.commit()
#
# Items2 = models.Items(name="Peach Cotton Lady's Slippers", image="56fd6c5839cc1.jpg",
#                               description=" Cotton cozy slippers, made by hand, designed for comfort and fun. Great in the kitchen. ",
#                               quantity=10,
#                               price="3.99", short_description="Entree", SubCategory=SubCat2, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
# Items3 = models.Items(name="Baby Bib", image="56fd6bcc6c10d.jpg",
#                               description="Bright colors & sweet foxes wearing chevron sweaters and leg warmers, backed with soft "
#                                           "flannel soft flannel, will give your little one a stylish, functional, and fun Scarf Bib "
#                                           "to keep them dry, warm, and adorable! The slouchy cut of the cotton print side gives a safe"
#                                           " & dry stylish scarf look. This bib fits little ones from 3 months to 2 years old. "
#                                           "The closure is a KAMsnap. The petit bandeau in pic 2 is available separately.  ",
#                               quantity=10,
#                               price="7.99", short_description="Dessert", SubCategory=SubCat1, shop=Shop1)
#
# db.session.add(Items3)
# db.session.commit()
#
# Items4 = models.Items(name="Tatiana - Lacy edge rust hat", image="56fd6c91eebfb.jpg",
#                               description="Truly chic wool cap with lacy brim, in an warm rust. Open detail around mid-section."
#                                           " Measures 9\" deep by 20\" around. Coming soon in a variety of heathery shades and"
#                                           " striking colors!",
#                               quantity=10,
#                               price="5.99", short_description="Entree", SubCategory=SubCat3, shop=Shop1)
#
# db.session.add(Items4)
# db.session.commit()
#
# Items5 = models.Items(name="Baseball Potholder", image="56fd78fb66e6c.jpg",
#                               description="Play Ball! Time for baseball, peanuts and cracker jacks! This baseball potholder will "
#                                           "get you in the mood. It is hand-crocheted double-thick in acrylic yarn, which washes and "
#                                           "dries beautifully. A baseball fills the front on a red background. The back is plain red"
#                                           " and the potholder is trimmed in white with a hanging loop.",
#                               quantity=10,
#                               price="1.99", short_description="Beverage", SubCategory=SubCat2, shop=Shop1)
#
# db.session.add(Items5)
# db.session.commit()
#
# Items6 = models.Items(name="Fun drawstring bags", image="56fd6c6e53e5b.jpeg",
#                               description="Check out these fun bags! Great for the beach, gym, overnight, or anytime you need a bag!"
#                                           " Throw whatever you need in and be on your way! They are cute and have plenty of"
#                                           " room inside!",
#                               quantity=10,
#                               price=".99", short_description="Beverage", SubCategory=SubCat3, shop=Shop1)
#
# db.session.add(Items6)
# db.session.commit()
#
# Items7 = models.Items(name="Handmade Curley Bunny", image="56fd6b71e857f.jpg",
#                               description="This darling bunny is made of a white curley fleece fabric. This bunny is soo soft and"
#                                           " cuddley. He is 16\" in a sitting position. It is stuffed with the best qulity fiberfill"
#                                           " and is very soft and cuddly.",
#                               quantity=10,
#                               price="3.49", short_description="Entree", SubCategory=SubCat1, shop=Shop1)
#
# db.session.add(Items7)
# db.session.commit()
#
# Items8 = models.Items(name="Delicate & Dainty Pink Shells Crocheted Scarf", image="56fd6cb5b8342.jpg",
#                               description="Rows & rows of deep rose pink shells create this delicate & dainty scarf. Casual, "
#                                           "but yet elegant. Perfect for cool evenings....ideal for winter months to ward away"
#                                           " the cold. Long enough to wrap around your neck or just let it dangle down off your"
#                                           " shoulders. Measures 62\" by 5\" Hand wash in cold water & lay flat to dry for best"
#                                           " results when laundering.",
#                               quantity=10,
#                               price="5.99", short_description="Entree", SubCategory=SubCat2, shop=Shop1)
#
# db.session.add(Items8)
# db.session.commit()
#
#
# # Menu for Super Stir Fry
# Shop2 = models.Shop(shop_name="Waterstones", owner_name="Nezar Saleh", owner_email="nezar@gmail.com", mobile="0122222222", password="nezar123",
#                             shop_profile_pic="570269d9abbba.jpeg",
#                             shop_cover_pic="570269d9abbba.jpeg",
#                             description="Waterstones, formerly Waterstone's, is a British book retailer that operates 275 stores"
#                                         " and employs around 3,500 staff in the UK and Europe as of February 2014.")
#
# db.session.add(Shop2)
# db.session.commit()
#
# Items1 = models.Items(name="Pretty Infinity Scarf", image="56fd7d3954f14.jpg",
#                               description="Here is a pretty multi coloured infinity scarf, loosly knitted with a combination of "
#                                           "three Acrylic yarns, it is lightweight and just perfect for the Spring season. Great "
#                                           "for casual wear and to compliment a plainT shirt or sweater.",
#                               quantity=10,
#                               price="7.99", short_description="Entree", SubCategory=SubCat4, shop=Shop2)
#
# db.session.add(Items1)
# db.session.commit()
#
# Items2 = models.Items(
#     name="Fiery Red Infinity Scarf", image="56fd7b46d254c.jpg",
#     description="Here is a bright red infinity scarf, loosely knit with an Acrylic yarn. Quite a little show stopper "
#                 "which will compliment other red accessories perfectly. Wash on a cold/ delicates machine cycle. ",
#     price="25", quantity=10, short_description="Entree", SubCategory=SubCat2, shop=Shop2)
#
# db.session.add(Items2)
# db.session.commit()
#
# Items3 = models.Items(name="Burnt Orange and Beige Snood", image="56fd7b5a53420.jpg",
#                               description="Here is a chunky knitted snood, unisex and hand crafted in a comination of two yarns"
#                                           " 40% cotton and 60% acrylic. Multi coloured in a burnt orange and beige, great for colder"
#                                           " evenings. Can be washed on a cold gentle cycle.",
#                               quantity=10,
#                               price="15", short_description="Entree", SubCategory=SubCat3, shop=Shop2)
#
# db.session.add(Items3)
# db.session.commit()
#
# Items4 = models.Items(name="Blue Bunny Set. Age 6/9 mos ", image="56fd7ce754b58.jpg",
#                               description="Hand crafted blue cardigan with matching hat and booties. Each has blue Bunny buttons, "
#                                           "just to add cuteness. Age 6- 9 months approximately. Material 100 % Acrylic. Can be machine"
#                                           " washed on a cool gentle/delicates cycle. ",
#                               quantity=10,
#                               price="12", short_description="Entree", SubCategory=SubCat1, shop=Shop2)
#
# db.session.add(Items4)
# db.session.commit()
#
# Items5 = models.Items(name="Multi Colored Booties Age 6 - 9 mos", image="56fd7b31b9c75.jpg",
#                               description="Here are a pair of multi colored Booties/Slippers, handcrafted in a 100% Acrylic yarn,"
#                                           " For ages approximately 6/9 mos and can be washed on a cool/delicate machine cycle.",
#                               quantity=10,
#                               price="14", short_description="Entree", SubCategory=SubCat1, shop=Shop2)
#
# db.session.add(Items5)
# db.session.commit()
#
# Items6 = models.Items(name="Knitted Small Fringed Rug", image="56fd7d027150f.jpg",
#                               description="Hand knitted small rug for any area, or may be used for covering a stroller or pet use."
#                                           " Very attractive by using a combination of both Acrylic and Cotton yarn in colors "
#                                           "of purple, green and white.",
#                               quantity=10,
#                               price="12", short_description="Entree", SubCategory=SubCat2, shop=Shop2)
#
# db.session.add(Items6)
# db.session.commit()
#
#
# # Menu for Panda Garden
# Shop1 = models.Shop(shop_name="Helzberg", owner_name="Nora Amer", owner_email="nora@gmail.com.com", mobile="0122222222", password="nora123",
#                             shop_profile_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
#                             shop_cover_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
#                             description="Helzberg Diamonds is a jewelry retailer founded in 1915 by Morris Helzberg that has 234"
#                                         " stores in the United States.\\par Jewelry")
#
# db.session.add(Shop1)
# db.session.commit()
#
# Items1 = models.Items(name="Lavender floral mask", image="56fd7d5f68e66.jpg",
#                               description="This is lovely mask decorated with silk floral petals and acrylic gems and finished"
#                                           " with sheer ribbon for ties. It is playful enough for Trick-or-treater, yet sophisticated"
#                                           " enough for elegant Halloween ball.",
#                               quantity=10,
#                               price="8.99", short_description="Entree", SubCategory=SubCat4, shop=Shop1)
#
# db.session.add(Items1)
# db.session.commit()
#
# Items2 = models.Items(name="White Hibiscus wreath with white ribbon, Wedding decor", image="56fd7d76b5222.jpg",
#                               description="This lovely 24 inch grapevine wreath decorated with premium silk Hibiscus flowers,"
#                                           " variegated ivy silk white ribbon, Lavender and purple sheer ribbon for accent."
#                                           " This gorgeous wreath would also make a beautiful wedding decor ",
#                               quantity=10,
#                               price="6.99", short_description="Appetizer", SubCategory=SubCat4, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
# Items3 = models.Items(name="Feather Butterfly Bouquet", image="",
#                               description="Included also are circular round 10mm crystals.  Handle is then wrapped in satin ribbon"
#                                           " and adorned with swarovski crystals for a finished look.  These can also be made to top "
#                                           "cakes of all kinds, or a table centerpieces.",
#                               quantity=10,
#                               price="9.95", short_description="Entree", SubCategory=SubCat1, shop=Shop1)
#
# db.session.add(Items3)
# db.session.commit()
#
# Items4 = models.Items(name="Real Pressed Blue Larkspur", image="56fd7da452ac5.jpg",
#                               description="Pressed flower motif rectangular glass paperweight with real pressed blue larkspur"
#                                           " as the focal point, makes a long-lasting gift. Not just for holding down papers -"
#                                           " this lovely display makes a wonderful botanical keepsakes. Especially popular as"
#                                           " a gift for the business professional and people with a home office. Great for table"
#                                           " and shelf displays too! 2 3/4\" by 4 1/4\" by 5/8\" high. Includes separate information"
#                                           " slip about the flower included and what makes this paperweight so special.",
#                               quantity=10,
#                               price="6.99", short_description="Entree", SubCategory=SubCat4, shop=Shop1)
#
# db.session.add(Items4)
# db.session.commit()
#
# Items2 = models.Items(name="Completed Cross Stitch Picture of a Bouquet of Daisies", image="56fd7dc03c073.jpg",
#                               description="This professionally stitched cross stitch picture does not depict your ordinary"
#                                           " white daisies, but the colourful mixture of blue, red and yellow petals in this"
#                                           " bouquet of daisies. All cross stitches are done in the same direction and with even"
#                                           " tension on white Aida fabric with quality cotton flosses. It is brand new from a "
#                                           "clean and smoke free environment. This is a very beautiful completed cross stitch"
#                                           " and will look great when matted and framed.",
#                               quantity=10,
#                               price="9.50", short_description="Entree", SubCategory=SubCat4, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
#
# # Menu for Thyme for that
# Shop1 = models.Shop(shop_name="Paul Parkman", owner_name="Ebrahim Arafa", owner_email="hema@gameil.com", mobile="0122222222", password="hema123",
#                             shop_profile_pic="57026a063ba27.jpg",
#                             shop_cover_pic="57026a063ba27.jpg",
#                             description="A represents a sophisticated brand of luxury man’s footwear which never loses sight of "
#                                         "the real art of handcrafting and enhances the personality of those experiencing the brand.")
#
# db.session.add(Shop1)
# db.session.commit()
#
# Items1 = models.Items(name="Paul Parkman Men's Brown Crocodile Embossed Tassel Loafer", image="",
#                               description="Brown hand painted crocodile embossed leather upper Natural antiqued leather sole."
#                                           " Bordeaux leather lining. Tassel loafer, slip-on style men's shoes.",
#                               quantity=10,
#                               price="200.99", short_description="Dessert", SubCategory=SubCat6, shop=Shop1)
#
# db.session.add(Items1)
# db.session.commit()
#
# Items2 = models.Items(name="Paul Parkman Men's Captoe ", image="",
#                               description="Description : Men's Captoe Oxfords - "
#                                           "Navy / Beige Hand-Painted Suede Upper "
#                                           "and Leather Sole", quantity=10,
#                               price="500.99", short_description="Entree", SubCategory=SubCat6, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
# Items3 = models.Items(name="Paul Parkman Men's Side Handsewn Tassel", image="",
#                               description="Side hand-sewn tassel loafer Slip-on style men's shoes. Green hand painted leather"
#                                           " upper Leather sole and bordeaux leather lining.",
#                               quantity=10,
#                               price="400.50", short_description="Dessert", SubCategory=SubCat6, shop=Shop1)
#
# db.session.add(Items3)
# db.session.commit()
#
# Items4 = models.Items(name="Paul Parkman Men's Reddish Camel Medallion", image="",
#                               description="Medallion Toe Handmade Oxfords Goodyear welted, double leather sole Reddish Camel"
#                                           " hand painted leather upper Bordeaux leather lining. Leather wrapped beige laces with"
#                                           " four eyelet",
#                               quantity=10,
#                               price="600.95", short_description="Appetizer", SubCategory=SubCat6, shop=Shop1)
#
# db.session.add(Items4)
# db.session.commit()
#
# Items5 = models.Items(name="Paul Parkman Men's Captoe Oxfords Brown Hand Painted Shoes", image="",
#                               description="Side handsewn captoe oxford style men's handmade shoes. Brown hand painted leather"
#                                           " upper with leather sole and bordeaux leather lining.  This is a made-to-order product."
#                                           " Please allow 15 days for the delivery",
#                               quantity=10,
#                               price="700.95", short_description="Entree", SubCategory=SubCat6, shop=Shop1)
#
# db.session.add(Items5)
# db.session.commit()
#
# Items2 = models.Items(name="Paul Parkman Men's Captoe Oxfords Black Shoes", image="",
#                               description="Side handsewn captoe "
#                                           "oxford style men's handmade"
#                                           " shoes. Black hand painted "
#                                           "leather upper with leather"
#                                           " sole and bordeaux leather"
#                                           " lining.",
#                               quantity=10,
#                               price="600.80", short_description="Entree", SubCategory=SubCat6, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
#
# # Menu for Tony's Bistro
# Shop1 = models.Shop(shop_name="Handmade Birdhouses", owner_name="Ahmed El-Mahalawy", owner_email="ahmed@gmail.com", mobile="0122222222", password="ahmed123",
#                             shop_profile_pic="57026a18d0c48.png",
#                             shop_cover_pic="57026a18d0c48.png",
#                             description="Hand crafted birdhouses made with 100% recycled materials. Old fences, pallets and "
#                                         "free materials are used to build these custom designed birdhouses. Been building birdhouses"
#                                         " for many years.")
#
# db.session.add(Shop1)
# db.session.commit()
#
# Items1 = models.Items(name="Feeding or Nesting Shelf", image="",
#                               description="This is a bird nesting or feeding shelf. Natural wood finish and weathered."
#                                           " Handcrafted and designed by me. Great for Robins or Morning Dove. Can be placed"
#                                           " on a long pole or hung from house.", quantity=10,
#                               price="13.95", short_description="Entree", SubCategory=SubCat5, shop=Shop1)
#
# db.session.add(Items1)
# db.session.commit()
#
# Items2 = models.Items(name="Finch Birdhouse", image="",
#                               description="This is a specially designed Finch birdhouse."
#                                           " Should be mount on a long pole 10’ – 15’ off "
#                                           "of the ground. The finch will enter through a hidden"
#                                           " opening at the rear of the birdhouse.", quantity=10,
#                               price="4.95", short_description="Entree", SubCategory=SubCat5, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
# Items3 = models.Items(name="Round Green Birdhouse", image="",
#                               description="This is a round 6.25” and 12” tall birdhouse."
#                                           " Made from recycled materials. It has an old "
#                                           "rusted spiral wire perch. Green with white stripes."
#                                           " Should be hung and out of the wind.",
#                               quantity=10,
#                               price="6.95", short_description="Entree", SubCategory=SubCat5, shop=Shop1)
#
# db.session.add(Items3)
# db.session.commit()
#
# Items4 = models.Items(name="Tree Birdhouse", image="", quantity=10,
#                               description="Tree Birdhouse, made with 4 pieces, to create the tree. And a nesting box round"
#                                           " with screws, so it can be removed for easy cleaning. 10 ?” W x 11” D x 15” H Weight: "
#                                           "3 pounds", price="3.95", short_description="Dessert", SubCategory=SubCat5,
#                               shop=Shop1)
#
# db.session.add(Items4)
# db.session.commit()
#
# Items5 = models.Items(name="Recycled wooden slates and rusting metal straps", image="",
#                               description="Wooden slates and rusting metal straps give this duplex birdhouse a unique look."
#                                           " Each end is different, one end “BRICKS” the other “WOODEN STONES”, also recycled wood.",
#                               quantity=10,
#                               price="7.95", short_description="Entree", SubCategory=SubCat5, shop=Shop1)
#
# db.session.add(Items5)
# db.session.commit()
#
#
# # Menu for Andala's
# Shop1 = models.Shop(shop_name="At Home", owner_name="Ehab Hashem", owner_email="ehab@gmail.com", mobile="0122222222", password="ehab123",
#                             shop_profile_pic="57026a2ba5e1a.jpg",
#                             shop_cover_pic="57026a2ba5e1a.jpg",
#                             description="At Home is a privately held home decor retail chain based in Plano, Texas. Owned "
#                                         "and operated by At Home Group Inc.")
#
# db.session.add(Shop1)
# db.session.commit()
#
# Items1 = models.Items(name="Midnight bling", image="",
#                               description="This set of jars are ready to add some bling to your home. Using broken pieces "
#                                           "of jewelry, I added rhinestones and a piece from a bracelet to these once spaghetti"
#                                           " sauce jars. I love spaghetti :)",
#                               quantity=10,
#                               price="9.95", short_description="Entree", SubCategory=SubCat7, shop=Shop1)
#
# db.session.add(Items1)
# db.session.commit()
#
# Items2 = models.Items(name="Squiggly lines, dots and whatever else", image="",
#                               description="My \"Squiggly lines, dots"
#                                           " and whatever else\" design "
#                                           "is back! This black and white"
#                                           " jar will add decor to your home"
#                                           " with its unique design."
#                                           " Hand painted and coated with "
#                                           "liquid varnish.",
#                               quantity=10,
#                               price="7.95", short_description="Entree", SubCategory=SubCat7, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
# Items3 = models.Items(name="A Trail in the Forest", image="",
#                               description="This glass beer bottle is like a forest..."
#                                           "one can get lost just looking at it. Hand painted "
#                                           "and decorated using beads, this bottle is sure to "
#                                           "be a conversation piece. Great for table"
#                                           " centerpieces or a bookshelf. ",
#                               quantity=10,
#                               price="6.50", short_description="Appetizer", SubCategory=SubCat7, shop=Shop1)
#
# db.session.add(Items3)
# db.session.commit()
#
# Items4 = models.Items(name="Buzz buzz", image="",
#                               description="What's that sound? Where is it coming from? A bee in its "
#                                           "beehive...well not exactly. This former honey jar is now"
#                                           " a blinged out work of art. The \"gold\" accent jewelry"
#                                           " is not real gold and is glued to the jar.", quantity=10,
#                               price="6.75", short_description="Appetizer", SubCategory=SubCat7, shop=Shop1)
#
# db.session.add(Items4)
# db.session.commit()
#
# Items2 = models.Items(name="His Eyes are on the Sparrow", image="",
#                               description="I like to call this a \"freestyle paint "
#                                           "doodle\" that I painted on a glass coffee jar"
#                                           ". And yes I love coffee :) The stokes"
#                                           " remind me of birds and the dots are like "
#                                           "eyes. This work of art could be a gift for"
#                                           " a religious event or be an addition to one's"
#                                           " home decor.",
#                               quantity=10,
#                               price="7.00", short_description="Entree", SubCategory=SubCat7, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
#
# # Menu for Auntie Ann's
# Shop1 = models.Shop(shop_name="Kirkland's Home", owner_name="Eslam Abo El-Fotoh", owner_email="eslam@gmail.com.com", mobile="0122222222", password="eslam123",
#                             shop_profile_pic="57026a3b52a10.png",
#                             shop_cover_pic="57026a3b52a10.png",
#                             description="Kirkland's, Inc. is a United States retail chain that sells home decor, specializing in"
#                                         " furnishings, accessories and gifts.")
#
# db.session.add(Shop1)
# db.session.commit()
#
# Items9 = models.Items(name="Leaf - MooDooNano paper", image="",
#                               description="Material Our current production offers a portfolio of eco design lamps made of a "
#                                           "special laminated MooDooNano paper, which is being constantly developed in cooperation"
#                                           " with NanoGraph paper mill.", quantity=10,
#                               price="8.99", short_description="Entree", SubCategory=SubCat8, shop=Shop1)
#
# db.session.add(Items9)
# db.session.commit()
#
# Items1 = models.Items(name="Valentine's Heart - MooDoo Lamp", image="",
#                               description="The beautiful lamp for everybody who wants to spread love and light.  "
#                                           "Lamp shade is made out of resistant, laminated paper.",
#                               quantity=10,
#                               price="2.99", short_description="Dessert", SubCategory=SubCat8, shop=Shop1)
#
# db.session.add(Items1)
# db.session.commit()
#
# Items2 = models.Items(name="Leaf - MooDooNano paper", image="",
#                               description="Material Our current production offers a portfolio of eco design lamps made "
#                                           "of a special laminated MooDooNano paper, which is being constantly developed in"
#                                           " cooperation with NanoGraph paper mill.",
#                               quantity=10,
#                               price="10.95", short_description="Entree", SubCategory=SubCat8, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
# Items3 = models.Items(name="Literary Lampshade #2", image="",
#                               description="This literary lampshade was created using Part I of Madame Bovary. "
#                                           "I included pictures from the novel. When the light shines through the pictures "
#                                           "it casts a lovely glow.", quantity=10,
#                               price="7.50", short_description="Appetizer", SubCategory=SubCat8, shop=Shop1)
#
# db.session.add(Items3)
# db.session.commit()
#
# Items4 = models.Items(name="MooDoo Lamp", image="",
#                               description="The beautiful lamp for everybody who wants to spread love and light.",
#                               quantity=10,
#                               price="8.95", short_description="Entree", SubCategory=SubCat8, shop=Shop1)
#
# db.session.add(Items4)
# db.session.commit()
#
# Items2 = models.Items(name="Leaf - MooDooNano paper design lamp on wire stand", image="",
#                               description="Guard is a knight."
#                                           " Active,"
#                                           " the invincible "
#                                           "explorer of everything"
#                                           " on the outside."
#                                           " Bringing activity,"
#                                           " the feeling of "
#                                           "security and safety"
#                                           " into households."
#                                           " A delightful visit "
#                                           "that will please. "
#                                           "Available also on "
#                                           "wooden stand...",
#                               quantity=10,
#                               price="9.50", short_description="Entree", SubCategory=SubCat8, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
# Items10 = models.Items(name="Literary Lampshade, \"Emma\" by Jane Austen", image="",
#                                description="Emma by Jane Austen "
#                                            " I used pages from "
#                                            "a pre-1918 edition of "
#                                            "the classic English novel,"
#                                            " Emma.  The top and bottom"
#                                            " of the shade are trimmed "
#                                            "with a rich rust coloured"
#                                            " ribbon topped with"
#                                            " hand-sewn, beaded black "
#                                            "velvet ribbon. "
#                                            " A beautiful addition"
#                                            " to any home!",
#                                quantity=10,
#                                price="1.99", short_description="Dessert", SubCategory=SubCat8, shop=Shop1)
#
# db.session.add(Items10)
# db.session.commit()
#
#
# # Menu for Cocina Y Amor
# Shop1 = models.Shop(shop_name="rue21", owner_name="Ahmed Maher", owner_email="maher@gameil.com", mobile="0122222222", password="maher123",
#                             shop_profile_pic="57026a6fa4e6d.jpeg",
#                             shop_cover_pic="57026a6fa4e6d.jpeg",
#                             description="rue21 Inc., formerly known as Pennsylvania Fashions Inc., is headquartered in the Pittsburgh"
#                                         " suburb of Warrendale, Pennsylvania.")
#
# db.session.add(Shop1)
# db.session.commit()
#
# Items1 = models.Items(name="knit leaf coasters", image="",
#                               description="These mug rugs are inspired by nature,bring the outdoors in with these handmade leaf"
#                                           " shape coasters, that could double as a dish cloth.", quantity=10,
#                               price="5.95", short_description="Entree", SubCategory=SubCat3, shop=Shop1)
#
# db.session.add(Items1)
# db.session.commit()
#
# Items2 = models.Items(name="nerdy knit coasters", image="",
#                               description="This is for a set of coasters featuring the water tribe symbol from the Avatar:"
#                                           " the last airbender. This is the perfect, subtle, gift for anime fans.",
#                               quantity=10,
#                               price="7.99", short_description="Entree", SubCategory=SubCat5, shop=Shop1)
#
# db.session.add(Items2)
# db.session.commit()
#
# Shop1 = models.Shop(shop_name="Ross Dress for Less", owner_name="Mohamed El-Gazzar", owner_email="gazzar@gameil.com", mobile="0122222222", password="gazzar123",
#                             shop_profile_pic="57026a8492608.jpg",
#                             shop_cover_pic="57026a8492608.jpg",
#                             description="Ross Stores, Inc., is an American chain of off-price department stores headquartered in "
#                                         "Dublin, California, operating under the name Ross Dress for Less. It is the largest"
#                                         " off-price retailer in the United States.")
# db.session.add(Shop1)
# db.session.commit()
#
# Items1 = models.Items(name="Chantrelle Toast", image="",
#                               description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
#                               quantity=10,
#                               price="5.95", short_description="Appetizer", SubCategory=SubCat2, shop=Shop1)
#
# db.session.add(Items1)
# db.session.commit()
#
# Items1 = models.Items(name="Guanciale Chawanmushi", quantity=10, image="",
#                               description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
#                               price="6.95", short_description="Dessert", SubCategory=SubCat4, shop=Shop1)
#
# db.session.add(Items1)
# db.session.commit()
#
# Items1 = models.Items(name="Lemon Curd Ice Cream Sandwich", image="",
#                               description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
#                               quantity=10,
#                               price="4.25", short_description="Dessert", SubCategory=SubCat3, shop=Shop1)
#
# db.session.add(Items1)
# db.session.commit()
#
# print "added menu items!"
