---
title: "PlaceCategory class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-placecategory-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/PlaceCategory-class-sidebar.html">

<div>

# <span class="kind-class">PlaceCategory</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a category of place with different levels of granularity.

This class also defines a set of most commonly used categories.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-placecategory">PlaceCategory</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-id" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">id</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-id">id</a></span> <span class="signature">→ String</span>  
Place category ID. Gets the place category ID.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-name">name</a></span> <span class="signature">→ String?</span>  
Localised place category name. It is available only when when `PlaceCategory` is obtained from `Place`. That means that when `PlaceCategory` is constructed directly by the client, `name` is always `null`. Gets the localised place category name.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Properties

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-accommodation">accommodation</a></span> <span class="signature">→ String</span>  
Top level category for places offering lodging accommodations, dwellings or similar living quarters to travellers, such as hotels, motels, resorts, cruise ships and campgrounds.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-accommodationhotelmotel">accommodationHotelMotel</a></span> <span class="signature">→ String</span>  
A business that provides lodging or temporary living quarters.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-accommodationlodging">accommodationLodging</a></span> <span class="signature">→ String</span>  
A business that provides lodging to the public generally without room service.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-areasandbuildings">areasAndBuildings</a></span> <span class="signature">→ String</span>  
Top level category for places that are owned, operated or managed by municipalities, such as cities, towns, villages, boroughs and shires.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-areasandbuildingsoutdoorcomplex">areasAndBuildingsOutdoorComplex</a></span> <span class="signature">→ String</span>  
Outdoor areas or complexes with designations for specific businesses or interests.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-areasandbuildingsresidentaloffice">areasAndBuildingsResidentalOffice</a></span> <span class="signature">→ String</span>  
Areas and buildings designated for residential or office use.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandcommercialservices">businessAndCommercialServices</a></span> <span class="signature">→ String</span>  
Businesses that provide a service or product for use by other businesses.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandconsumerservices">businessAndConsumerServices</a></span> <span class="signature">→ String</span>  
An organization that provides consumer services for a variety of products for used by the public.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservices">businessAndServices</a></span> <span class="signature">→ String</span>  
Top level category for places that provide professional services to other businesses, such as printing, photocopying, graphic design, marketing, advertising and other general business services.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicesatm">businessAndServicesAtm</a></span> <span class="signature">→ String</span>  
A computer terminal that allows bank customers to deposit, withdraw, or transfer funds without the assistance of a bank teller.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicesbanking">businessAndServicesBanking</a></span> <span class="signature">→ String</span>  
Businesses that specialize in the maintenance, lending, exchange, or issuance of money.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicescardealersales">businessAndServicesCarDealerSales</a></span> <span class="signature">→ String</span>  
Businesses that sell new automobiles and motorcycles.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicescarrental">businessAndServicesCarRental</a></span> <span class="signature">→ String</span>  
Businesses that rent or lease automobiles.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicescarrepairservices">businessAndServicesCarRepairServices</a></span> <span class="signature">→ String</span>  
Businesses that provide automotive repair services.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicescommunicationmedia">businessAndServicesCommunicationMedia</a></span> <span class="signature">→ String</span>  
Businesses that provide communication services.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicesevchargingstation">businessAndServicesEvChargingStation</a></span> <span class="signature">→ String</span>  
Businesses that provide recharging services for electric vehicles.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicesfuelingstation">businessAndServicesFuelingStation</a></span> <span class="signature">→ String</span>  
Businesses that sell fuel for vehicles, such as petrol, electricity etc.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicesindustry">businessAndServicesIndustry</a></span> <span class="signature">→ String</span>  
Businesses that employ people in and around the city in which it is located.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicesmoneycash">businessAndServicesMoneyCash</a></span> <span class="signature">→ String</span>  
Businesses that provide money related services.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicespetrolgasolinestation">businessAndServicesPetrolGasolineStation</a></span> <span class="signature">→ String</span>  
Businesses that sell fuel, oil, and other motoring supplies.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicespolicefireemergency">businessAndServicesPoliceFireEmergency</a></span> <span class="signature">→ String</span>  
Municipal emergency services.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicespostoffice">businessAndServicesPostOffice</a></span> <span class="signature">→ String</span>  
An office or station that receives, sorts, dispatches and delivers mail to a specific area or region.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicestouristinformation">businessAndServicesTouristInformation</a></span> <span class="signature">→ String</span>  
Businesses that provide a variety of information for visiting tourists, such as event schedules, lodging/accommodations, restaurants, attractions and more.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-businessandservicestrucksemidealer">businessAndServicesTruckSemiDealer</a></span> <span class="signature">→ String</span>  
Business that sell or service trucks and tractor trailers.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-eatanddrink">eatAndDrink</a></span> <span class="signature">→ String</span>  
Top level category for places where food or beverages are prepared or served.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-eatanddrinkcoffeetea">eatAndDrinkCoffeeTea</a></span> <span class="signature">→ String</span>  
An establishment that sells drinks, such as coffee and tea, as well as refreshments.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-eatanddrinkrestaurant">eatAndDrinkRestaurant</a></span> <span class="signature">→ String</span>  
An establishment that prepares and serves refreshments and prepared meals.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-facilities">facilities</a></span> <span class="signature">→ String</span>  
Top level category for places associated with specialized facilities, such as sports venues, government buildings, health care centers and other types of facilities.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-facilitieseducation">facilitiesEducation</a></span> <span class="signature">→ String</span>  
Facilities that are used for educational purposes including training, coaching, universities and more.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-facilitieseventspaces">facilitiesEventSpaces</a></span> <span class="signature">→ String</span>  
An area or facility used for the hosting of fairs and conventions.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-facilitiesgovernmentcommunitty">facilitiesGovernmentCommunitty</a></span> <span class="signature">→ String</span>  
A Place where government services are provided.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-facilitieshospitalhealthcare">facilitiesHospitalHealthcare</a></span> <span class="signature">→ String</span>  
Facilities that include dental offices, hospitals, nursing homes and other health care-related services.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-facilitieslibrary">facilitiesLibrary</a></span> <span class="signature">→ String</span>  
Facilities that offer books, periodicals, audio, video and other material for public use.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-facilitiesother">facilitiesOther</a></span> <span class="signature">→ String</span>  
Facilities with miscellaneous uses such as Clubhouses, Offices, and Registration Offices.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-facilitiesparking">facilitiesParking</a></span> <span class="signature">→ String</span>  
Area or building used for parking cars.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-facilitiesschool">facilitiesSchool</a></span> <span class="signature">→ String</span>  
Educational facilities that include primary schools, secondary schools and more.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-facilitiesvenuesports">facilitiesVenueSports</a></span> <span class="signature">→ String</span>  
A facility used for individual and team sports including recreational sports.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-goingoutcinema">goingOutCinema</a></span> <span class="signature">→ String</span>  
An establishment that shows movies through screen projection.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-goingoutentertainment">goingOutEntertainment</a></span> <span class="signature">→ String</span>  
Top level category for places commonly associated with entertainment, such as bars, cinemas, theatres, casinos and night clubs.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-goingoutgamblinglotterybetting">goingOutGamblingLotteryBetting</a></span> <span class="signature">→ String</span>  
An establishment that provides gambling entertainment.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-goingoutnightlife">goingOutNightlife</a></span> <span class="signature">→ String</span>  
An establishment that provides evening entertainment and usually serves alcoholic beverages.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-goingouttheatremusicculture">goingOutTheatreMusicCulture</a></span> <span class="signature">→ String</span>  
An establishment where various types of performing arts are presented.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-leisureandoutdoor">leisureAndOutdoor</a></span> <span class="signature">→ String</span>  
Top level category for places that are designated for sports, recreation, parking, beaches and other leisure and outdoor activities.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-leisureother">leisureOther</a></span> <span class="signature">→ String</span>  
A park that contains rides and/or other entertainment which may be based on a central theme.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-leisureoutdoorrecreation">leisureOutdoorRecreation</a></span> <span class="signature">→ String</span>  
Public land preserved and maintained for recreational use.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-naturalandgeographical">naturalAndGeographical</a></span> <span class="signature">→ String</span>  
Top level category for natural or man-made areas of regional importance, such as bodies of water, mountains, forested areas and other geographic areas.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-naturalandgeographicalbodyofwater">naturalAndGeographicalBodyOfWater</a></span> <span class="signature">→ String</span>  
A natural and geographical feature of the earth's surface that is covered with water, such as a lake, river, stream or ocean.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-naturalandgeographicalforesthealthothervegetation">naturalAndGeographicalForestHealthOtherVegetation</a></span> <span class="signature">→ String</span>  
A dense growth of trees, open uncultivated land or other large masses of vegetation.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-naturalandgeographicalmountainorhill">naturalAndGeographicalMountainOrHill</a></span> <span class="signature">→ String</span>  
A natural and geographical feature that is higher than the surrounding land.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-naturalandgeographicalother">naturalAndGeographicalOther</a></span> <span class="signature">→ String</span>  
A feature not classified as a Body of Water, Mountain or Hill, Undersea Feature, or Forest, Heath or Other Vegetation.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-naturalandgeographicalunderseafeature">naturalAndGeographicalUnderseaFeature</a></span> <span class="signature">→ String</span>  
A natural or artificial feature that is below sea level.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shopping">shopping</a></span> <span class="signature">→ String</span>  
Top level category for places where consumer goods are commonly sold, such as clothing stores, grocery stores, hardware stores and other types of shopping centers.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shoppingbookstore">shoppingBookstore</a></span> <span class="signature">→ String</span>  
A business that sells books, magazines and other reading material.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shoppingclothingandaccesories">shoppingClothingAndAccesories</a></span> <span class="signature">→ String</span>  
A business that sells apparel items, garments or fashion accessories for men, women, and children.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shoppingconsumergoods">shoppingConsumerGoods</a></span> <span class="signature">→ String</span>  
A business that sells a variety of products targeted to consumers.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shoppingconveniencestore">shoppingConvenienceStore</a></span> <span class="signature">→ String</span>  
An establishment that sells groceries, candy, toiletries, soft drinks, tobacco products, newspapers and other products.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shoppingdepartmentstore">shoppingDepartmentStore</a></span> <span class="signature">→ String</span>  
A business that sells a wide variety of merchandise that is organized by product or service departments.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shoppingdrugstorepharmacy">shoppingDrugstorePharmacy</a></span> <span class="signature">→ String</span>  
A business that sells medications, toiletry items and other retail cosmetics.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shoppingelectronics">shoppingElectronics</a></span> <span class="signature">→ String</span>  
A business that sells consumer electronics and electronic entertainment equipment.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shoppingfoodanddrink">shoppingFoodAndDrink</a></span> <span class="signature">→ String</span>  
A business that sells specialty products of a particular type of food or beverage.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shoppinghairandbeauty">shoppingHairAndBeauty</a></span> <span class="signature">→ String</span>  
A business that provides hair styling and personal appearance services. Places in this category may also sell hair products and other related cosmetic items.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shoppinghardwarehousegarden">shoppingHardwareHouseGarden</a></span> <span class="signature">→ String</span>  
A business that sells crafts, gardening, remodeling, or decorating items for the home.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-shoppingmallcomplex">shoppingMallComplex</a></span> <span class="signature">→ String</span>  
A complex of businesses that are co-located and share common services.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-sightsandmuseums">sightsAndMuseums</a></span> <span class="signature">→ String</span>  
Top level category for places of special interest, such as common tourist attractions, museums and places of worship.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-sightslandmarkattraction">sightsLandmarkAttraction</a></span> <span class="signature">→ String</span>  
A designated area of special interest to tourists.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-sightsmuseum">sightsMuseum</a></span> <span class="signature">→ String</span>  
An establishment dedicated to the preservation and exhibition of artistic, historical, or scientific artifacts.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-sightsreligiousplace">sightsReligiousPlace</a></span> <span class="signature">→ String</span>  
An establishment special religious significance or where religious services are held.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-transport">transport</a></span> <span class="signature">→ String</span>  
Top level category for places commonly associated with pedestrian and cargo transport facilities, including airports, rail yards and seaports.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-transportairport">transportAirport</a></span> <span class="signature">→ String</span>  
A designated area that serves various aspects of aviation related sports, including gliders, recreational aircraft and model airplanes.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-transportcargo">transportCargo</a></span> <span class="signature">→ String</span>  
A facility that handles some aspect of the transportation of cargo freight.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-transportpublic">transportPublic</a></span> <span class="signature">→ String</span>  
A facility for travelers who are travelling between stops on public transport.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-placecategory-transportrestarea">transportRestArea</a></span> <span class="signature">→ String</span>  
An establishment along a motorway (controlled access road) that provides restrooms and parking.

<div class="features">

<span class="feature">final</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

