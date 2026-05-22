---
title: "Untitled"
slug: "sdk-for-flutter-explore-search-placecategory-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PlaceCategory-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">PlaceCategory class</li>
</ol>
<div class="self-name">PlaceCategory</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/PlaceCategory-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PlaceCategory class abstract</h1></div>
<section class="desc markdown">
<p>Represents a category of place with different levels of granularity.</p>
<p>This class also defines a set of most commonly used categories.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PlaceCategory">
/sdk-for-flutter-explore-search-placecategory-placecategory(String id)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-search-placecategory-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-explore-search-placecategory-id
→ String
</dt>
<dd>
  Place category ID.
Gets the place category ID.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="name">
/sdk-for-flutter-explore-search-placecategory-name
→ String?
</dt>
<dd>
  Localised place category name.
It is available only when when <code>PlaceCategory</code> is obtained from <code>Place</code>.
That means that when <code>PlaceCategory</code> is constructed directly by the client,
<code>name</code> is always <code>null</code>.
Gets the localised place category name.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-search-placecategory-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-search-placecategory-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-search-placecategory-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-explore-search-placecategory-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-properties">
<h2>Static Properties</h2>
<dl class="properties">
<dt class="property" id="accommodation">
/sdk-for-flutter-explore-search-placecategory-accommodation
→ String
</dt>
<dd>
  Top level category for places offering lodging accommodations, dwellings or similar living quarters to travellers,
such as hotels, motels, resorts, cruise ships and campgrounds.
  <div class="features">final</div>
</dd>
<dt class="property" id="accommodationHotelMotel">
/sdk-for-flutter-explore-search-placecategory-accommodationhotelmotel
→ String
</dt>
<dd>
  A business that provides lodging or temporary living quarters.
  <div class="features">final</div>
</dd>
<dt class="property" id="accommodationLodging">
/sdk-for-flutter-explore-search-placecategory-accommodationlodging
→ String
</dt>
<dd>
  A business that provides lodging to the public generally without room service.
  <div class="features">final</div>
</dd>
<dt class="property" id="areasAndBuildings">
/sdk-for-flutter-explore-search-placecategory-areasandbuildings
→ String
</dt>
<dd>
  Top level category for places that are owned, operated or managed by municipalities,
such as cities, towns, villages, boroughs and shires.
  <div class="features">final</div>
</dd>
<dt class="property" id="areasAndBuildingsOutdoorComplex">
/sdk-for-flutter-explore-search-placecategory-areasandbuildingsoutdoorcomplex
→ String
</dt>
<dd>
  Outdoor areas or complexes with designations for specific businesses or interests.
  <div class="features">final</div>
</dd>
<dt class="property" id="areasAndBuildingsResidentalOffice">
/sdk-for-flutter-explore-search-placecategory-areasandbuildingsresidentaloffice
→ String
</dt>
<dd>
  Areas and buildings designated for residential or office use.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndCommercialServices">
/sdk-for-flutter-explore-search-placecategory-businessandcommercialservices
→ String
</dt>
<dd>
  Businesses that provide a service or product for use by other businesses.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndConsumerServices">
/sdk-for-flutter-explore-search-placecategory-businessandconsumerservices
→ String
</dt>
<dd>
  An organization that provides consumer services for a variety of products for used by the public.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServices">
/sdk-for-flutter-explore-search-placecategory-businessandservices
→ String
</dt>
<dd>
  Top level category for places that provide professional services to other businesses,
such as printing, photocopying, graphic design, marketing, advertising and other general business services.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesAtm">
/sdk-for-flutter-explore-search-placecategory-businessandservicesatm
→ String
</dt>
<dd>
  A computer terminal that allows bank customers to deposit, withdraw, or transfer funds without the assistance of a bank teller.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesBanking">
/sdk-for-flutter-explore-search-placecategory-businessandservicesbanking
→ String
</dt>
<dd>
  Businesses that specialize in the maintenance, lending, exchange, or issuance of money.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesCarDealerSales">
/sdk-for-flutter-explore-search-placecategory-businessandservicescardealersales
→ String
</dt>
<dd>
  Businesses that sell new automobiles and motorcycles.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesCarRental">
/sdk-for-flutter-explore-search-placecategory-businessandservicescarrental
→ String
</dt>
<dd>
  Businesses that rent or lease automobiles.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesCarRepairServices">
/sdk-for-flutter-explore-search-placecategory-businessandservicescarrepairservices
→ String
</dt>
<dd>
  Businesses that provide automotive repair services.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesCommunicationMedia">
/sdk-for-flutter-explore-search-placecategory-businessandservicescommunicationmedia
→ String
</dt>
<dd>
  Businesses that provide communication services.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesEvChargingStation">
/sdk-for-flutter-explore-search-placecategory-businessandservicesevchargingstation
→ String
</dt>
<dd>
  Businesses that provide recharging services for electric vehicles.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesFuelingStation">
/sdk-for-flutter-explore-search-placecategory-businessandservicesfuelingstation
→ String
</dt>
<dd>
  Businesses that sell fuel for vehicles, such as petrol, electricity etc.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesIndustry">
/sdk-for-flutter-explore-search-placecategory-businessandservicesindustry
→ String
</dt>
<dd>
  Businesses that employ people in and around the city in which it is located.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesMoneyCash">
/sdk-for-flutter-explore-search-placecategory-businessandservicesmoneycash
→ String
</dt>
<dd>
  Businesses that provide money related services.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesPetrolGasolineStation">
/sdk-for-flutter-explore-search-placecategory-businessandservicespetrolgasolinestation
→ String
</dt>
<dd>
  Businesses that sell fuel, oil, and other motoring supplies.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesPoliceFireEmergency">
/sdk-for-flutter-explore-search-placecategory-businessandservicespolicefireemergency
→ String
</dt>
<dd>
  Municipal emergency services.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesPostOffice">
/sdk-for-flutter-explore-search-placecategory-businessandservicespostoffice
→ String
</dt>
<dd>
  An office or station that receives, sorts, dispatches and delivers mail to a specific area or region.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesTouristInformation">
/sdk-for-flutter-explore-search-placecategory-businessandservicestouristinformation
→ String
</dt>
<dd>
  Businesses that provide a variety of information for visiting tourists,
such as event schedules, lodging/accommodations, restaurants, attractions and more.
  <div class="features">final</div>
</dd>
<dt class="property" id="businessAndServicesTruckSemiDealer">
/sdk-for-flutter-explore-search-placecategory-businessandservicestrucksemidealer
→ String
</dt>
<dd>
  Business that sell or service trucks and tractor trailers.
  <div class="features">final</div>
</dd>
<dt class="property" id="eatAndDrink">
/sdk-for-flutter-explore-search-placecategory-eatanddrink
→ String
</dt>
<dd>
  Top level category for places where food or beverages are prepared or served.
  <div class="features">final</div>
</dd>
<dt class="property" id="eatAndDrinkCoffeeTea">
/sdk-for-flutter-explore-search-placecategory-eatanddrinkcoffeetea
→ String
</dt>
<dd>
  An establishment that sells drinks, such as coffee and tea, as well as refreshments.
  <div class="features">final</div>
</dd>
<dt class="property" id="eatAndDrinkRestaurant">
/sdk-for-flutter-explore-search-placecategory-eatanddrinkrestaurant
→ String
</dt>
<dd>
  An establishment that prepares and serves refreshments and prepared meals.
  <div class="features">final</div>
</dd>
<dt class="property" id="facilities">
/sdk-for-flutter-explore-search-placecategory-facilities
→ String
</dt>
<dd>
  Top level category for places associated with specialized facilities,
such as sports venues, government buildings, health care centers and other types of facilities.
  <div class="features">final</div>
</dd>
<dt class="property" id="facilitiesEducation">
/sdk-for-flutter-explore-search-placecategory-facilitieseducation
→ String
</dt>
<dd>
  Facilities that are used for educational purposes including training, coaching, universities and more.
  <div class="features">final</div>
</dd>
<dt class="property" id="facilitiesEventSpaces">
/sdk-for-flutter-explore-search-placecategory-facilitieseventspaces
→ String
</dt>
<dd>
  An area or facility used for the hosting of fairs and conventions.
  <div class="features">final</div>
</dd>
<dt class="property" id="facilitiesGovernmentCommunitty">
/sdk-for-flutter-explore-search-placecategory-facilitiesgovernmentcommunitty
→ String
</dt>
<dd>
  A Place where government services are provided.
  <div class="features">final</div>
</dd>
<dt class="property" id="facilitiesHospitalHealthcare">
/sdk-for-flutter-explore-search-placecategory-facilitieshospitalhealthcare
→ String
</dt>
<dd>
  Facilities that include dental offices, hospitals, nursing homes and other health care-related services.
  <div class="features">final</div>
</dd>
<dt class="property" id="facilitiesLibrary">
/sdk-for-flutter-explore-search-placecategory-facilitieslibrary
→ String
</dt>
<dd>
  Facilities that offer books, periodicals, audio, video and other material for public use.
  <div class="features">final</div>
</dd>
<dt class="property" id="facilitiesOther">
/sdk-for-flutter-explore-search-placecategory-facilitiesother
→ String
</dt>
<dd>
  Facilities with miscellaneous uses such as Clubhouses, Offices, and Registration Offices.
  <div class="features">final</div>
</dd>
<dt class="property" id="facilitiesParking">
/sdk-for-flutter-explore-search-placecategory-facilitiesparking
→ String
</dt>
<dd>
  Area or building used for parking cars.
  <div class="features">final</div>
</dd>
<dt class="property" id="facilitiesSchool">
/sdk-for-flutter-explore-search-placecategory-facilitiesschool
→ String
</dt>
<dd>
  Educational facilities that include primary schools, secondary schools and more.
  <div class="features">final</div>
</dd>
<dt class="property" id="facilitiesVenueSports">
/sdk-for-flutter-explore-search-placecategory-facilitiesvenuesports
→ String
</dt>
<dd>
  A facility used for individual and team sports including recreational sports.
  <div class="features">final</div>
</dd>
<dt class="property" id="goingOutCinema">
/sdk-for-flutter-explore-search-placecategory-goingoutcinema
→ String
</dt>
<dd>
  An establishment that shows movies through screen projection.
  <div class="features">final</div>
</dd>
<dt class="property" id="goingOutEntertainment">
/sdk-for-flutter-explore-search-placecategory-goingoutentertainment
→ String
</dt>
<dd>
  Top level category for places commonly associated with entertainment,
such as bars, cinemas, theatres, casinos and night clubs.
  <div class="features">final</div>
</dd>
<dt class="property" id="goingOutGamblingLotteryBetting">
/sdk-for-flutter-explore-search-placecategory-goingoutgamblinglotterybetting
→ String
</dt>
<dd>
  An establishment that provides gambling entertainment.
  <div class="features">final</div>
</dd>
<dt class="property" id="goingOutNightlife">
/sdk-for-flutter-explore-search-placecategory-goingoutnightlife
→ String
</dt>
<dd>
  An establishment that provides evening entertainment and usually serves alcoholic beverages.
  <div class="features">final</div>
</dd>
<dt class="property" id="goingOutTheatreMusicCulture">
/sdk-for-flutter-explore-search-placecategory-goingouttheatremusicculture
→ String
</dt>
<dd>
  An establishment where various types of performing arts are presented.
  <div class="features">final</div>
</dd>
<dt class="property" id="leisureAndOutdoor">
/sdk-for-flutter-explore-search-placecategory-leisureandoutdoor
→ String
</dt>
<dd>
  Top level category for places that are designated for sports, recreation, parking, beaches
and other leisure and outdoor activities.
  <div class="features">final</div>
</dd>
<dt class="property" id="leisureOther">
/sdk-for-flutter-explore-search-placecategory-leisureother
→ String
</dt>
<dd>
  A park that contains rides and/or other entertainment which may be based on a central theme.
  <div class="features">final</div>
</dd>
<dt class="property" id="leisureOutdoorRecreation">
/sdk-for-flutter-explore-search-placecategory-leisureoutdoorrecreation
→ String
</dt>
<dd>
  Public land preserved and maintained for recreational use.
  <div class="features">final</div>
</dd>
<dt class="property" id="naturalAndGeographical">
/sdk-for-flutter-explore-search-placecategory-naturalandgeographical
→ String
</dt>
<dd>
  Top level category for natural or man-made areas of regional importance,
such as bodies of water, mountains, forested areas and other geographic areas.
  <div class="features">final</div>
</dd>
<dt class="property" id="naturalAndGeographicalBodyOfWater">
/sdk-for-flutter-explore-search-placecategory-naturalandgeographicalbodyofwater
→ String
</dt>
<dd>
  A natural and geographical feature of the earth's surface that is covered with water, such as a lake, river, stream or ocean.
  <div class="features">final</div>
</dd>
<dt class="property" id="naturalAndGeographicalForestHealthOtherVegetation">
/sdk-for-flutter-explore-search-placecategory-naturalandgeographicalforesthealthothervegetation
→ String
</dt>
<dd>
  A dense growth of trees, open uncultivated land or other large masses of vegetation.
  <div class="features">final</div>
</dd>
<dt class="property" id="naturalAndGeographicalMountainOrHill">
/sdk-for-flutter-explore-search-placecategory-naturalandgeographicalmountainorhill
→ String
</dt>
<dd>
  A natural and geographical feature that is higher than the surrounding land.
  <div class="features">final</div>
</dd>
<dt class="property" id="naturalAndGeographicalOther">
/sdk-for-flutter-explore-search-placecategory-naturalandgeographicalother
→ String
</dt>
<dd>
  A feature not classified as a Body of Water, Mountain or Hill, Undersea Feature, or Forest, Heath or Other Vegetation.
  <div class="features">final</div>
</dd>
<dt class="property" id="naturalAndGeographicalUnderseaFeature">
/sdk-for-flutter-explore-search-placecategory-naturalandgeographicalunderseafeature
→ String
</dt>
<dd>
  A natural or artificial feature that is below sea level.
  <div class="features">final</div>
</dd>
<dt class="property" id="shopping">
/sdk-for-flutter-explore-search-placecategory-shopping
→ String
</dt>
<dd>
  Top level category for places where consumer goods are commonly sold,
such as clothing stores, grocery stores, hardware stores and other types of shopping centers.
  <div class="features">final</div>
</dd>
<dt class="property" id="shoppingBookstore">
/sdk-for-flutter-explore-search-placecategory-shoppingbookstore
→ String
</dt>
<dd>
  A business that sells books, magazines and other reading material.
  <div class="features">final</div>
</dd>
<dt class="property" id="shoppingClothingAndAccesories">
/sdk-for-flutter-explore-search-placecategory-shoppingclothingandaccesories
→ String
</dt>
<dd>
  A business that sells apparel items, garments or fashion accessories for men, women, and children.
  <div class="features">final</div>
</dd>
<dt class="property" id="shoppingConsumerGoods">
/sdk-for-flutter-explore-search-placecategory-shoppingconsumergoods
→ String
</dt>
<dd>
  A business that sells a variety of products targeted to consumers.
  <div class="features">final</div>
</dd>
<dt class="property" id="shoppingConvenienceStore">
/sdk-for-flutter-explore-search-placecategory-shoppingconveniencestore
→ String
</dt>
<dd>
  An establishment that sells groceries, candy, toiletries, soft drinks, tobacco products, newspapers and other products.
  <div class="features">final</div>
</dd>
<dt class="property" id="shoppingDepartmentStore">
/sdk-for-flutter-explore-search-placecategory-shoppingdepartmentstore
→ String
</dt>
<dd>
  A business that sells a wide variety of merchandise that is organized by product or service departments.
  <div class="features">final</div>
</dd>
<dt class="property" id="shoppingDrugstorePharmacy">
/sdk-for-flutter-explore-search-placecategory-shoppingdrugstorepharmacy
→ String
</dt>
<dd>
  A business that sells medications, toiletry items and other retail cosmetics.
  <div class="features">final</div>
</dd>
<dt class="property" id="shoppingElectronics">
/sdk-for-flutter-explore-search-placecategory-shoppingelectronics
→ String
</dt>
<dd>
  A business that sells consumer electronics and electronic entertainment equipment.
  <div class="features">final</div>
</dd>
<dt class="property" id="shoppingFoodAndDrink">
/sdk-for-flutter-explore-search-placecategory-shoppingfoodanddrink
→ String
</dt>
<dd>
  A business that sells specialty products of a particular type of food or beverage.
  <div class="features">final</div>
</dd>
<dt class="property" id="shoppingHairAndBeauty">
/sdk-for-flutter-explore-search-placecategory-shoppinghairandbeauty
→ String
</dt>
<dd>
  A business that provides hair styling and personal appearance services.
Places in this category may also sell hair products and other related cosmetic items.
  <div class="features">final</div>
</dd>
<dt class="property" id="shoppingHardwareHouseGarden">
/sdk-for-flutter-explore-search-placecategory-shoppinghardwarehousegarden
→ String
</dt>
<dd>
  A business that sells crafts, gardening, remodeling, or decorating items for the home.
  <div class="features">final</div>
</dd>
<dt class="property" id="shoppingMallComplex">
/sdk-for-flutter-explore-search-placecategory-shoppingmallcomplex
→ String
</dt>
<dd>
  A complex of businesses that are co-located and share common services.
  <div class="features">final</div>
</dd>
<dt class="property" id="sightsAndMuseums">
/sdk-for-flutter-explore-search-placecategory-sightsandmuseums
→ String
</dt>
<dd>
  Top level category for places of special interest,
such as common tourist attractions, museums and places of worship.
  <div class="features">final</div>
</dd>
<dt class="property" id="sightsLandmarkAttraction">
/sdk-for-flutter-explore-search-placecategory-sightslandmarkattraction
→ String
</dt>
<dd>
  A designated area of special interest to tourists.
  <div class="features">final</div>
</dd>
<dt class="property" id="sightsMuseum">
/sdk-for-flutter-explore-search-placecategory-sightsmuseum
→ String
</dt>
<dd>
  An establishment dedicated to the preservation and exhibition of artistic, historical, or scientific artifacts.
  <div class="features">final</div>
</dd>
<dt class="property" id="sightsReligiousPlace">
/sdk-for-flutter-explore-search-placecategory-sightsreligiousplace
→ String
</dt>
<dd>
  An establishment special religious significance or where religious services are held.
  <div class="features">final</div>
</dd>
<dt class="property" id="transport">
/sdk-for-flutter-explore-search-placecategory-transport
→ String
</dt>
<dd>
  Top level category for places commonly associated with pedestrian and cargo transport facilities,
including airports, rail yards and seaports.
  <div class="features">final</div>
</dd>
<dt class="property" id="transportAirport">
/sdk-for-flutter-explore-search-placecategory-transportairport
→ String
</dt>
<dd>
  A designated area that serves various aspects of aviation related sports, including gliders, recreational aircraft and model airplanes.
  <div class="features">final</div>
</dd>
<dt class="property" id="transportCargo">
/sdk-for-flutter-explore-search-placecategory-transportcargo
→ String
</dt>
<dd>
  A facility that handles some aspect of the transportation of cargo freight.
  <div class="features">final</div>
</dd>
<dt class="property" id="transportPublic">
/sdk-for-flutter-explore-search-placecategory-transportpublic
→ String
</dt>
<dd>
  A facility for travelers who are travelling between stops on public transport.
  <div class="features">final</div>
</dd>
<dt class="property" id="transportRestArea">
/sdk-for-flutter-explore-search-placecategory-transportrestarea
→ String
</dt>
<dd>
  An establishment along a motorway (controlled access road) that provides restrooms and parking.
  <div class="features">final</div>
</dd>
</dl>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">PlaceCategory class</li>
</ol>
<h5>search library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
