---
title: "PlaceCategory (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestplacecategory"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PlaceCategory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.search.PlaceCategory
------------------------------------------------------------------------
public final class PlaceCategory extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Represents a category of place with different levels of granularity. This class also defines a set of most commonly used categories.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [ACCOMMODATION](#ACCOMMODATION)

Top level category for places offering lodging accommodations, dwellings or similar living quarters to travellers, such as hotels, motels, resorts, cruise ships and campgrounds.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [ACCOMMODATION_HOTEL_MOTEL](#ACCOMMODATION_HOTEL_MOTEL)

A business that provides lodging or temporary living quarters.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [ACCOMMODATION_LODGING](#ACCOMMODATION_LODGING)

A business that provides lodging to the public generally without room service.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [AREAS_AND_BUILDINGS](#AREAS_AND_BUILDINGS)

Top level category for places that are owned, operated or managed by municipalities, such as cities, towns, villages, boroughs and shires.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX](#AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX)

Outdoor areas or complexes with designations for specific businesses or interests.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE](#AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE)

Areas and buildings designated for residential or office use.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_COMMERCIAL_SERVICES](#BUSINESS_AND_COMMERCIAL_SERVICES)

Businesses that provide a service or product for use by other businesses.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_CONSUMER_SERVICES](#BUSINESS_AND_CONSUMER_SERVICES)

An organization that provides consumer services for a variety of products for used by the public.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES](#BUSINESS_AND_SERVICES)

Top level category for places that provide professional services to other businesses, such as printing, photocopying, graphic design, marketing, advertising and other general business services.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_ATM](#BUSINESS_AND_SERVICES_ATM)

A computer terminal that allows bank customers to deposit, withdraw, or transfer funds without the assistance of a bank teller.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_BANKING](#BUSINESS_AND_SERVICES_BANKING)

Businesses that specialize in the maintenance, lending, exchange, or issuance of money.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_CAR_DEALER_SALES](#BUSINESS_AND_SERVICES_CAR_DEALER_SALES)

Businesses that sell new automobiles and motorcycles.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_CAR_RENTAL](#BUSINESS_AND_SERVICES_CAR_RENTAL)

Businesses that rent or lease automobiles.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES](#BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES)

Businesses that provide automotive repair services.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA](#BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA)

Businesses that provide communication services.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_EV_CHARGING_STATION](#BUSINESS_AND_SERVICES_EV_CHARGING_STATION)

Businesses that provide recharging services for electric vehicles.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_FUELING_STATION](#BUSINESS_AND_SERVICES_FUELING_STATION)

Businesses that sell fuel for vehicles, such as petrol, electricity etc.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_INDUSTRY](#BUSINESS_AND_SERVICES_INDUSTRY)

Businesses that employ people in and around the city in which it is located.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_MONEY_CASH](#BUSINESS_AND_SERVICES_MONEY_CASH)

Businesses that provide money related services.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION](#BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION)

Businesses that sell fuel, oil, and other motoring supplies.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY](#BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY)

Municipal emergency services.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_POST_OFFICE](#BUSINESS_AND_SERVICES_POST_OFFICE)

An office or station that receives, sorts, dispatches and delivers mail to a specific area or region.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_TOURIST_INFORMATION](#BUSINESS_AND_SERVICES_TOURIST_INFORMATION)

Businesses that provide a variety of information for visiting tourists, such as event schedules, lodging/accommodations, restaurants, attractions and more.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER](#BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER)

Business that sell or service trucks and tractor trailers.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [EAT_AND_DRINK](#EAT_AND_DRINK)

Top level category for places where food or beverages are prepared or served.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [EAT_AND_DRINK_COFFEE_TEA](#EAT_AND_DRINK_COFFEE_TEA)

An establishment that sells drinks, such as coffee and tea, as well as refreshments.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [EAT_AND_DRINK_RESTAURANT](#EAT_AND_DRINK_RESTAURANT)

An establishment that prepares and serves refreshments and prepared meals.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [FACILITIES](#FACILITIES)

Top level category for places associated with specialized facilities, such as sports venues, government buildings, health care centers and other types of facilities.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [FACILITIES_EDUCATION](#FACILITIES_EDUCATION)

Facilities that are used for educational purposes including training, coaching, universities and more.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [FACILITIES_EVENT_SPACES](#FACILITIES_EVENT_SPACES)

An area or facility used for the hosting of fairs and conventions.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [FACILITIES_GOVERNMENT_COMMUNITTY](#FACILITIES_GOVERNMENT_COMMUNITTY)

A Place where government services are provided.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [FACILITIES_HOSPITAL_HEALTHCARE](#FACILITIES_HOSPITAL_HEALTHCARE)

Facilities that include dental offices, hospitals, nursing homes and other health care-related services.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [FACILITIES_LIBRARY](#FACILITIES_LIBRARY)

Facilities that offer books, periodicals, audio, video and other material for public use.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [FACILITIES_OTHER](#FACILITIES_OTHER)

Facilities with miscellaneous uses such as Clubhouses, Offices, and Registration Offices.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [FACILITIES_PARKING](#FACILITIES_PARKING)

Area or building used for parking cars.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [FACILITIES_SCHOOL](#FACILITIES_SCHOOL)

Educational facilities that include primary schools, secondary schools and more.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [FACILITIES_VENUE_SPORTS](#FACILITIES_VENUE_SPORTS)

A facility used for individual and team sports including recreational sports.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [GOING_OUT_CINEMA](#GOING_OUT_CINEMA)

An establishment that shows movies through screen projection.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [GOING_OUT_ENTERTAINMENT](#GOING_OUT_ENTERTAINMENT)

Top level category for places commonly associated with entertainment, such as bars, cinemas, theatres, casinos and night clubs.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [GOING_OUT_GAMBLING_LOTTERY_BETTING](#GOING_OUT_GAMBLING_LOTTERY_BETTING)

An establishment that provides gambling entertainment.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [GOING_OUT_NIGHTLIFE](#GOING_OUT_NIGHTLIFE)

An establishment that provides evening entertainment and usually serves alcoholic beverages.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [GOING_OUT_THEATRE_MUSIC_CULTURE](#GOING_OUT_THEATRE_MUSIC_CULTURE)

An establishment where various types of performing arts are presented.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [LEISURE_AND_OUTDOOR](#LEISURE_AND_OUTDOOR)

Top level category for places that are designated for sports, recreation, parking, beaches and other leisure and outdoor activities.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [LEISURE_OTHER](#LEISURE_OTHER)

A park that contains rides and/or other entertainment which may be based on a central theme.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [LEISURE_OUTDOOR_RECREATION](#LEISURE_OUTDOOR_RECREATION)

Public land preserved and maintained for recreational use.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [NATURAL_AND_GEOGRAPHICAL](#NATURAL_AND_GEOGRAPHICAL)

Top level category for natural or man-made areas of regional importance, such as bodies of water, mountains, forested areas and other geographic areas.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER](#NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER)

A natural and geographical feature of the earth's surface that is covered with water, such as a lake, river, stream or ocean.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION](#NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION)

A dense growth of trees, open uncultivated land or other large masses of vegetation.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL](#NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL)

A natural and geographical feature that is higher than the surrounding land.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [NATURAL_AND_GEOGRAPHICAL_OTHER](#NATURAL_AND_GEOGRAPHICAL_OTHER)

A feature not classified as a Body of Water, Mountain or Hill, Undersea Feature, or Forest, Heath or Other Vegetation.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE](#NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE)

A natural or artificial feature that is below sea level.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING](#SHOPPING)

Top level category for places where consumer goods are commonly sold, such as clothing stores, grocery stores, hardware stores and other types of shopping centers.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING_BOOKSTORE](#SHOPPING_BOOKSTORE)

A business that sells books, magazines and other reading material.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING_CLOTHING_AND_ACCESORIES](#SHOPPING_CLOTHING_AND_ACCESORIES)

A business that sells apparel items, garments or fashion accessories for men, women, and children.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING_CONSUMER_GOODS](#SHOPPING_CONSUMER_GOODS)

A business that sells a variety of products targeted to consumers.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING_CONVENIENCE_STORE](#SHOPPING_CONVENIENCE_STORE)

An establishment that sells groceries, candy, toiletries, soft drinks, tobacco products, newspapers and other products.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING_DEPARTMENT_STORE](#SHOPPING_DEPARTMENT_STORE)

A business that sells a wide variety of merchandise that is organized by product or service departments.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING_DRUGSTORE_PHARMACY](#SHOPPING_DRUGSTORE_PHARMACY)

A business that sells medications, toiletry items and other retail cosmetics.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING_ELECTRONICS](#SHOPPING_ELECTRONICS)

A business that sells consumer electronics and electronic entertainment equipment.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING_FOOD_AND_DRINK](#SHOPPING_FOOD_AND_DRINK)

A business that sells specialty products of a particular type of food or beverage.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING_HAIR_AND_BEAUTY](#SHOPPING_HAIR_AND_BEAUTY)

A business that provides hair styling and personal appearance services.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING_HARDWARE_HOUSE_GARDEN](#SHOPPING_HARDWARE_HOUSE_GARDEN)

A business that sells crafts, gardening, remodeling, or decorating items for the home.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SHOPPING_MALL_COMPLEX](#SHOPPING_MALL_COMPLEX)

A complex of businesses that are co-located and share common services.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SIGHTS_AND_MUSEUMS](#SIGHTS_AND_MUSEUMS)

Top level category for places of special interest, such as common tourist attractions, museums and places of worship.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SIGHTS_LANDMARK_ATTACTION](#SIGHTS_LANDMARK_ATTACTION)

Deprecated.
Will be removed in v4.26.0.

  `static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SIGHTS_LANDMARK_ATTRACTION](#SIGHTS_LANDMARK_ATTRACTION)

A designated area of special interest to tourists.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SIGHTS_MUSEUM](#SIGHTS_MUSEUM)

An establishment dedicated to the preservation and exhibition of artistic, historical, or scientific artifacts.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [SIGHTS_RELIGIOUS_PLACE](#SIGHTS_RELIGIOUS_PLACE)

An establishment special religious significance or where religious services are held.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRANSPORT](#TRANSPORT)

Top level category for places commonly associated with pedestrian and cargo transport facilities, including airports, rail yards and seaports.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRANSPORT_AIRPORT](#TRANSPORT_AIRPORT)

A designated area that serves various aspects of aviation related sports, including gliders, recreational aircraft and model airplanes.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRANSPORT_CARGO](#TRANSPORT_CARGO)

A facility that handles some aspect of the transportation of cargo freight.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRANSPORT_PUBLIC](#TRANSPORT_PUBLIC)

A facility for travelers who are travelling between stops on public transport.

`static final `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [TRANSPORT_REST_AREA](#TRANSPORT_REST_AREA)

An establishment along a motorway (controlled access road) that provides restrooms and parking.

## Constructor Summary

Constructors

Constructor

  Description

  [PlaceCategory](#%3Cinit%3E(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` id)`

Creates a new instance of this class.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getId](#getId())`()`

Gets the place category ID.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getName](#getName())`()`

Gets the localised place category name.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### EAT_AND_DRINK

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EAT_AND_DRINK

    Top level category for places where food or beverages are prepared or served.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.EAT_AND_DRINK)

### EAT_AND_DRINK_RESTAURANT

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EAT_AND_DRINK_RESTAURANT

    An establishment that prepares and serves refreshments and prepared meals.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.EAT_AND_DRINK_RESTAURANT)

### EAT_AND_DRINK_COFFEE_TEA

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) EAT_AND_DRINK_COFFEE_TEA

    An establishment that sells drinks, such as coffee and tea, as well as refreshments.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.EAT_AND_DRINK_COFFEE_TEA)

### GOING_OUT_ENTERTAINMENT

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) GOING_OUT_ENTERTAINMENT

    Top level category for places commonly associated with entertainment, such as bars, cinemas, theatres, casinos and night clubs.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_ENTERTAINMENT)

### GOING_OUT_NIGHTLIFE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) GOING_OUT_NIGHTLIFE

    An establishment that provides evening entertainment and usually serves alcoholic beverages.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_NIGHTLIFE)

### GOING_OUT_CINEMA

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) GOING_OUT_CINEMA

    An establishment that shows movies through screen projection.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_CINEMA)

### GOING_OUT_THEATRE_MUSIC_CULTURE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) GOING_OUT_THEATRE_MUSIC_CULTURE

    An establishment where various types of performing arts are presented.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_THEATRE_MUSIC_CULTURE)

### GOING_OUT_GAMBLING_LOTTERY_BETTING

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) GOING_OUT_GAMBLING_LOTTERY_BETTING

    An establishment that provides gambling entertainment.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.GOING_OUT_GAMBLING_LOTTERY_BETTING)

### SIGHTS_AND_MUSEUMS

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SIGHTS_AND_MUSEUMS

    Top level category for places of special interest, such as common tourist attractions, museums and places of worship.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SIGHTS_AND_MUSEUMS)

### SIGHTS_LANDMARK_ATTACTION

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SIGHTS_LANDMARK_ATTACTION

    Deprecated.
Will be removed in v4.26.0. Please use SIGHTS_LANDMARK_ATTRACTION instead.

A designated area of special interest to tourists.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SIGHTS_LANDMARK_ATTACTION)

### SIGHTS_LANDMARK_ATTRACTION

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SIGHTS_LANDMARK_ATTRACTION

    A designated area of special interest to tourists.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SIGHTS_LANDMARK_ATTRACTION)

### SIGHTS_MUSEUM

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SIGHTS_MUSEUM

    An establishment dedicated to the preservation and exhibition of artistic, historical, or scientific artifacts.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SIGHTS_MUSEUM)

### SIGHTS_RELIGIOUS_PLACE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SIGHTS_RELIGIOUS_PLACE

    An establishment special religious significance or where religious services are held.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SIGHTS_RELIGIOUS_PLACE)

### NATURAL_AND_GEOGRAPHICAL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NATURAL_AND_GEOGRAPHICAL

    Top level category for natural or man-made areas of regional importance, such as bodies of water, mountains, forested areas and other geographic areas.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL)

### NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER

    A natural and geographical feature of the earth's surface that is covered with water, such as a lake, river, stream or ocean.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_BODY_OF_WATER)

### NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL

    A natural and geographical feature that is higher than the surrounding land.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_MOUNTAIN_OR_HILL)

### NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE

    A natural or artificial feature that is below sea level.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_UNDERSEA_FEATURE)

### NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION

    A dense growth of trees, open uncultivated land or other large masses of vegetation.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_FOREST_HEALTH_OTHER_VEGETATION)

### NATURAL_AND_GEOGRAPHICAL_OTHER

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) NATURAL_AND_GEOGRAPHICAL_OTHER

    A feature not classified as a Body of Water, Mountain or Hill, Undersea Feature, or Forest, Heath or Other Vegetation.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.NATURAL_AND_GEOGRAPHICAL_OTHER)

### TRANSPORT

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRANSPORT

    Top level category for places commonly associated with pedestrian and cargo transport facilities, including airports, rail yards and seaports.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.TRANSPORT)

### TRANSPORT_AIRPORT

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRANSPORT_AIRPORT

    A designated area that serves various aspects of aviation related sports, including gliders, recreational aircraft and model airplanes.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_AIRPORT)

### TRANSPORT_PUBLIC

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRANSPORT_PUBLIC

    A facility for travelers who are travelling between stops on public transport.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_PUBLIC)

### TRANSPORT_CARGO

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRANSPORT_CARGO

    A facility that handles some aspect of the transportation of cargo freight.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_CARGO)

### TRANSPORT_REST_AREA

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) TRANSPORT_REST_AREA

    An establishment along a motorway (controlled access road) that provides restrooms and parking.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.TRANSPORT_REST_AREA)

### ACCOMMODATION

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ACCOMMODATION

    Top level category for places offering lodging accommodations, dwellings or similar living quarters to travellers, such as hotels, motels, resorts, cruise ships and campgrounds.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.ACCOMMODATION)

### ACCOMMODATION_HOTEL_MOTEL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ACCOMMODATION_HOTEL_MOTEL

    A business that provides lodging or temporary living quarters.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.ACCOMMODATION_HOTEL_MOTEL)

### ACCOMMODATION_LODGING

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ACCOMMODATION_LODGING

    A business that provides lodging to the public generally without room service.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.ACCOMMODATION_LODGING)

### LEISURE_AND_OUTDOOR

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LEISURE_AND_OUTDOOR

    Top level category for places that are designated for sports, recreation, parking, beaches and other leisure and outdoor activities.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.LEISURE_AND_OUTDOOR)

### LEISURE_OUTDOOR_RECREATION

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LEISURE_OUTDOOR_RECREATION

    Public land preserved and maintained for recreational use.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.LEISURE_OUTDOOR_RECREATION)

### LEISURE_OTHER

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) LEISURE_OTHER

    A park that contains rides and/or other entertainment which may be based on a central theme.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.LEISURE_OTHER)

### SHOPPING

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING

    Top level category for places where consumer goods are commonly sold, such as clothing stores, grocery stores, hardware stores and other types of shopping centers.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING)

### SHOPPING_CONVENIENCE_STORE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING_CONVENIENCE_STORE

    An establishment that sells groceries, candy, toiletries, soft drinks, tobacco products, newspapers and other products.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING_CONVENIENCE_STORE)

### SHOPPING_MALL_COMPLEX

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING_MALL_COMPLEX

    A complex of businesses that are co-located and share common services.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING_MALL_COMPLEX)

### SHOPPING_DEPARTMENT_STORE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING_DEPARTMENT_STORE

    A business that sells a wide variety of merchandise that is organized by product or service departments.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING_DEPARTMENT_STORE)

### SHOPPING_FOOD_AND_DRINK

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING_FOOD_AND_DRINK

    A business that sells specialty products of a particular type of food or beverage.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING_FOOD_AND_DRINK)

### SHOPPING_DRUGSTORE_PHARMACY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING_DRUGSTORE_PHARMACY

    A business that sells medications, toiletry items and other retail cosmetics.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING_DRUGSTORE_PHARMACY)

### SHOPPING_ELECTRONICS

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING_ELECTRONICS

    A business that sells consumer electronics and electronic entertainment equipment.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING_ELECTRONICS)

### SHOPPING_HARDWARE_HOUSE_GARDEN

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING_HARDWARE_HOUSE_GARDEN

    A business that sells crafts, gardening, remodeling, or decorating items for the home.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING_HARDWARE_HOUSE_GARDEN)

### SHOPPING_BOOKSTORE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING_BOOKSTORE

    A business that sells books, magazines and other reading material.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING_BOOKSTORE)

### SHOPPING_CLOTHING_AND_ACCESORIES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING_CLOTHING_AND_ACCESORIES

    A business that sells apparel items, garments or fashion accessories for men, women, and children.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING_CLOTHING_AND_ACCESORIES)

### SHOPPING_CONSUMER_GOODS

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING_CONSUMER_GOODS

    A business that sells a variety of products targeted to consumers.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING_CONSUMER_GOODS)

### SHOPPING_HAIR_AND_BEAUTY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) SHOPPING_HAIR_AND_BEAUTY

    A business that provides hair styling and personal appearance services. Places in this category may also sell hair products and other related cosmetic items.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.SHOPPING_HAIR_AND_BEAUTY)

### BUSINESS_AND_SERVICES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES

    Top level category for places that provide professional services to other businesses, such as printing, photocopying, graphic design, marketing, advertising and other general business services.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES)

### BUSINESS_AND_SERVICES_BANKING

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_BANKING

    Businesses that specialize in the maintenance, lending, exchange, or issuance of money.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_BANKING)

### BUSINESS_AND_SERVICES_ATM

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_ATM

    A computer terminal that allows bank customers to deposit, withdraw, or transfer funds without the assistance of a bank teller.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_ATM)

### BUSINESS_AND_SERVICES_MONEY_CASH

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_MONEY_CASH

    Businesses that provide money related services.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_MONEY_CASH)

### BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA

    Businesses that provide communication services.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_COMMUNICATION_MEDIA)

### BUSINESS_AND_COMMERCIAL_SERVICES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_COMMERCIAL_SERVICES

    Businesses that provide a service or product for use by other businesses.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_COMMERCIAL_SERVICES)

### BUSINESS_AND_SERVICES_INDUSTRY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_INDUSTRY

    Businesses that employ people in and around the city in which it is located.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_INDUSTRY)

### BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY

    Municipal emergency services.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_POLICE_FIRE_EMERGENCY)

### BUSINESS_AND_CONSUMER_SERVICES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_CONSUMER_SERVICES

    An organization that provides consumer services for a variety of products for used by the public.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_CONSUMER_SERVICES)

### BUSINESS_AND_SERVICES_POST_OFFICE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_POST_OFFICE

    An office or station that receives, sorts, dispatches and delivers mail to a specific area or region.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_POST_OFFICE)

### BUSINESS_AND_SERVICES_TOURIST_INFORMATION

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_TOURIST_INFORMATION

    Businesses that provide a variety of information for visiting tourists, such as event schedules, lodging/accommodations, restaurants, attractions and more.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_TOURIST_INFORMATION)

### BUSINESS_AND_SERVICES_FUELING_STATION

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_FUELING_STATION

    Businesses that sell fuel for vehicles, such as petrol, electricity etc.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_FUELING_STATION)

### BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION

    Businesses that sell fuel, oil, and other motoring supplies.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_PETROL_GASOLINE_STATION)

### BUSINESS_AND_SERVICES_EV_CHARGING_STATION

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_EV_CHARGING_STATION

    Businesses that provide recharging services for electric vehicles.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION)

### BUSINESS_AND_SERVICES_CAR_DEALER_SALES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_CAR_DEALER_SALES

    Businesses that sell new automobiles and motorcycles.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_CAR_DEALER_SALES)

### BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES

    Businesses that provide automotive repair services.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_CAR_REPAIR_SERVICES)

### BUSINESS_AND_SERVICES_CAR_RENTAL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_CAR_RENTAL

    Businesses that rent or lease automobiles.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_CAR_RENTAL)

### BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER

    Business that sell or service trucks and tractor trailers.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.BUSINESS_AND_SERVICES_TRUCK_SEMI_DEALER)

### FACILITIES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FACILITIES

    Top level category for places associated with specialized facilities, such as sports venues, government buildings, health care centers and other types of facilities.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.FACILITIES)

### FACILITIES_HOSPITAL_HEALTHCARE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FACILITIES_HOSPITAL_HEALTHCARE

    Facilities that include dental offices, hospitals, nursing homes and other health care-related services.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.FACILITIES_HOSPITAL_HEALTHCARE)

### FACILITIES_GOVERNMENT_COMMUNITTY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FACILITIES_GOVERNMENT_COMMUNITTY

    A Place where government services are provided.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.FACILITIES_GOVERNMENT_COMMUNITTY)

### FACILITIES_EDUCATION

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FACILITIES_EDUCATION

    Facilities that are used for educational purposes including training, coaching, universities and more.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.FACILITIES_EDUCATION)

### FACILITIES_SCHOOL

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FACILITIES_SCHOOL

    Educational facilities that include primary schools, secondary schools and more.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.FACILITIES_SCHOOL)

### FACILITIES_LIBRARY

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FACILITIES_LIBRARY

    Facilities that offer books, periodicals, audio, video and other material for public use.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.FACILITIES_LIBRARY)

### FACILITIES_EVENT_SPACES

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FACILITIES_EVENT_SPACES

    An area or facility used for the hosting of fairs and conventions.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.FACILITIES_EVENT_SPACES)

### FACILITIES_PARKING

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FACILITIES_PARKING

    Area or building used for parking cars.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.FACILITIES_PARKING)

### FACILITIES_VENUE_SPORTS

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FACILITIES_VENUE_SPORTS

    A facility used for individual and team sports including recreational sports.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.FACILITIES_VENUE_SPORTS)

### FACILITIES_OTHER

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) FACILITIES_OTHER

    Facilities with miscellaneous uses such as Clubhouses, Offices, and Registration Offices.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.FACILITIES_OTHER)

### AREAS_AND_BUILDINGS

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AREAS_AND_BUILDINGS

    Top level category for places that are owned, operated or managed by municipalities, such as cities, towns, villages, boroughs and shires.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.AREAS_AND_BUILDINGS)

### AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX

    Outdoor areas or complexes with designations for specific businesses or interests.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.AREAS_AND_BUILDINGS_OUTDOOR_COMPLEX)

### AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE

    Areas and buildings designated for residential or office use.
See Also:
    - [Constant Field Values](sdk-for-android-explore-api-reference-latestconstant-values#com.here.sdk.search.PlaceCategory.AREAS_AND_BUILDINGS_RESIDENTAL_OFFICE)

## Constructor Details

  - (java.lang.String)" class="section detail">

### PlaceCategory

public PlaceCategory(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id)

    Creates a new instance of this class.
Parameters:
    `id` -

    Place category ID. The HERE places category system provides three levels of granularity:

    1.  Level 1 represents high level groupings, such as "Eat and drink". Their IDs take the form "xxx", for example "100".
    2.  Level 2 represents logical sub-groups or domains, such as "Eat and Drink / Restaurant". Their IDs take the form "xxx-xxxx", for example "100-1000".
    3.  Level 3 provides the greatest level of granularity about place categorization, such as "Eat and Drink / Restaurant / Casual Dining". Their IDs take the form "xxx-xxxx-xxxx", for example "100-1000-0001". The category ID can be provided as one of the predefined values, such as [`EAT_AND_DRINK_RESTAURANT`](#EAT_AND_DRINK_RESTAURANT) or as a literal string that matches one of the category IDs defined by the HERE Search service. Only level 1 and 2 category IDs are predefined. The complete list of supported category IDs, including level 3, can be found online: https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html.

## Method Details

### getId

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getId()

    Gets the place category ID.
Returns:
    Place category ID.

### getName

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getName()

    Gets the localised place category name.

    It is available only when when `PlaceCategory` is obtained from `Place`. That means that when `PlaceCategory` is constructed directly by the client, `name` is always `null`.
Returns:
    Localised place category name.
