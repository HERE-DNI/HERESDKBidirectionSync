---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-search-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- search-library.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">search.dart</li>
</ol>
<div class="self-name">search</div>
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
<div class="main-content" data-above-sidebar="" data-below-sidebar="search/search-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>search library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="Address">
/sdk-for-flutter-navigate-search-address-class
</dt>
<dd>
  Information about the address of a location.
</dd>
<dt id="AddressQuery">
/sdk-for-flutter-navigate-search-addressquery-class
</dt>
<dd>
  The options to specify an address query.
</dd>
<dt id="BusinessDetails">
/sdk-for-flutter-navigate-search-businessdetails-class
</dt>
<dd>
  Contains place details such as contacts, opening hours and some electro vehicle info.
</dd>
<dt id="CategoryQuery">
/sdk-for-flutter-navigate-search-categoryquery-class
</dt>
<dd>
  The options to specify a query by categories.
</dd>
<dt id="CategoryQueryArea">
/sdk-for-flutter-navigate-search-categoryqueryarea-class
</dt>
<dd>
  Area to perform search on.
</dd>
<dt id="Contact">
/sdk-for-flutter-navigate-search-contact-class
</dt>
<dd>
  Represents contact information.
</dd>
<dt id="DateRange">
/sdk-for-flutter-navigate-search-daterange-class
</dt>
<dd>
  Represents the date range when the tariff element is valid.
</dd>
<dt id="Details">
/sdk-for-flutter-navigate-search-details-class
</dt>
<dd>
  Contains details of a specific place, such as contact information,
opening hours and assigned categories.
</dd>
<dt id="EmailAddress">
/sdk-for-flutter-navigate-search-emailaddress-class
</dt>
<dd>
  Represents data related to specific email address.
</dd>
<dt id="EMobilityServiceProvider">
/sdk-for-flutter-navigate-search-emobilityserviceprovider-class
</dt>
<dd>
  eMSP (e-Mobility Service Provider) for which the EV station operator has EV roaming agreements.
</dd>
<dt id="EnergyMix">
/sdk-for-flutter-navigate-search-energymix-class
</dt>
<dd>
  Represents details on the energy supplied at the charging location.
</dd>
<dt id="EnergySource">
/sdk-for-flutter-navigate-search-energysource-class
</dt>
<dd>
  Energy source of EV charging point.
</dd>
<dt id="EnvironmentalImpact">
/sdk-for-flutter-navigate-search-environmentalimpact-class
</dt>
<dd>
  Represents environmental impact for an environmental impact category.
</dd>
<dt id="EVChargingConnector">
/sdk-for-flutter-navigate-search-evchargingconnector-class
</dt>
<dd>
  Represents a connector at the charging point.
</dd>
<dt id="EVChargingConnectorGroup">
/sdk-for-flutter-navigate-search-evchargingconnectorgroup-class
</dt>
<dd>
  Represents the connector group at the charging location.
</dd>
<dt id="EVChargingConnectorReference">
/sdk-for-flutter-navigate-search-evchargingconnectorreference-class
</dt>
<dd>
  Represents a pairing of an EVSE and its connector(s) that belong to a group.
</dd>
<dt id="EVChargingDurationRange">
/sdk-for-flutter-navigate-search-evchargingdurationrange-class
</dt>
<dd>
  Duration of the charging session when the tariff element is valid, in seconds.
</dd>
<dt id="EVChargingLocation">
/sdk-for-flutter-navigate-search-evcharginglocation-class
</dt>
<dd>
  An electric vehicle (EV) charging location.
</dd>
<dt id="EVChargingOpeningHours">
/sdk-for-flutter-navigate-search-evchargingopeninghours-class
</dt>
<dd>
  Represents the times when the EVSEs at the charging location can be accessed for charging.
</dd>
<dt id="EVChargingOpeningHoursException">
/sdk-for-flutter-navigate-search-evchargingopeninghoursexception-class
</dt>
<dd>
  Represents exceptions to the regular opening hours schedule for EV charging locations,
such as special closures or extended hours.
</dd>
<dt id="EVChargingOpeningHoursSchedule">
/sdk-for-flutter-navigate-search-evchargingopeninghoursschedule-class
</dt>
<dd>
  Opening hours schedule for EV charging locations, represented by a list of days of the week
during which the location is open in the given time periods.
</dd>
<dt id="EVChargingOperator">
/sdk-for-flutter-navigate-search-evchargingoperator-class
</dt>
<dd>
  Represents name and optionally other details about operator, suboperator, or e-Mobility service provider.
</dd>
<dt id="EVChargingPool">
/sdk-for-flutter-navigate-search-evchargingpool-class
</dt>
<dd>
  A charging pool for electric vehicles is an area equipped with one or more charging stations.
</dd>
<dt id="EVChargingPoolDetails">
/sdk-for-flutter-navigate-search-evchargingpooldetails-class
</dt>
<dd>
  Electric vehicle charging pool details.
</dd>
<dt id="EVChargingStation">
/sdk-for-flutter-navigate-search-evchargingstation-class
</dt>
<dd>
  Group of connectors for electric vehicles (EVs), defined by a common charging connector type and
maximum power level.
</dd>
<dt id="EVChargingTariff">
/sdk-for-flutter-navigate-search-evchargingtariff-class
</dt>
<dd>
  Tariffs provide detailed pricing information for charging electric vehicles at a specific location.
</dd>
<dt id="EVChargingTariffElement">
/sdk-for-flutter-navigate-search-evchargingtariffelement-class
</dt>
<dd>
  Represents a tariff element, which defines how pricing is applied.
</dd>
<dt id="EVChargingTariffElementCondition">
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-class
</dt>
<dd>
  Condition that the charging session needs to meet to apply the tariff element.
</dd>
<dt id="EVChargingTariffPriceComponent">
/sdk-for-flutter-navigate-search-evchargingtariffpricecomponent-class
</dt>
<dd>
  Represents the price component of an EV charging tariff.
</dd>
<dt id="EVChargingTariffRequest">
/sdk-for-flutter-navigate-search-evchargingtariffrequest-class
</dt>
<dd>
  Represents a search option to choose the eMSP or CPO whose tariff should be included in the response.
</dd>
<dt id="EVChargingTruckRestriction">
/sdk-for-flutter-navigate-search-evchargingtruckrestriction-class
</dt>
<dd>
  Represents access restrictions for trucks and light commercial vehicles.
</dd>
<dt id="Evse">
/sdk-for-flutter-navigate-search-evse-class
</dt>
<dd>
  Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.
</dd>
<dt id="EVSearchEngine">
/sdk-for-flutter-navigate-search-evsearchengine-class
</dt>
<dd>
  The <code>EVSearchEngine</code> API provides detailed information about charging locations.
</dd>
<dt id="EVSearchInterface">
/sdk-for-flutter-navigate-search-evsearchinterface-class
</dt>
<dd>
  Provides the abstract class for the <code>EVSearchEngine</code>.
</dd>
<dt id="EVSearchOptions">
/sdk-for-flutter-navigate-search-evsearchoptions-class
</dt>
<dd>
  Encapsulates additional options that control the behavior of <code>EVSearchEngine</code>.
</dd>
<dt id="EVSEConnector">
/sdk-for-flutter-navigate-search-evseconnector-class
</dt>
<dd>
  EVSE connector.
</dd>
<dt id="EVSEInfo">
/sdk-for-flutter-navigate-search-evseinfo-class
</dt>
<dd>
  Represents an EVSE at the charging point.
</dd>
<dt id="FuelAdditive">
/sdk-for-flutter-navigate-search-fueladditive-class
</dt>
<dd>
  Contains fuel additive information for generic fuel type.
</dd>
<dt id="FuelStation">
/sdk-for-flutter-navigate-search-fuelstation-class
</dt>
<dd>
  Contains information about a specific fuel station.
</dd>
<dt id="GenericFuel">
/sdk-for-flutter-navigate-search-genericfuel-class
</dt>
<dd>
  Contains generic fuel type info of fuel station.
</dd>
<dt id="GeoPlace">
/sdk-for-flutter-navigate-search-geoplace-class
</dt>
<dd>
  GeoPlace struct represents a location object:
such as a country, a city, a point of interest (POI) etc.
</dd>
<dt id="IndexRange">
/sdk-for-flutter-navigate-search-indexrange-class
</dt>
<dd>
  Holds information to which part of the text, input query was matched.
</dd>
<dt id="LandlinePhone">
/sdk-for-flutter-navigate-search-landlinephone-class
</dt>
<dd>
  Represents data related to specific landline phone number.
</dd>
<dt id="LocationDetails">
/sdk-for-flutter-navigate-search-locationdetails-class
</dt>
<dd>
  Contains geographical info about location
</dd>
<dt id="MobilePhone">
/sdk-for-flutter-navigate-search-mobilephone-class
</dt>
<dd>
  Represents data related to specific mobile phone number.
</dd>
<dt id="MyPlaces">
/sdk-for-flutter-navigate-search-myplaces-class
</dt>
<dd>
  Provides means to populate personal places data source.
</dd>
<dt id="OfflineSearchEngine">
/sdk-for-flutter-navigate-search-offlinesearchengine-class
</dt>
<dd>
  The OfflineSearchEngine works without internet and unlocks the search and geocoding
capabilities of HERE services to provide developers with unmatched flexibility
to create differentiating location-enabled applications.
</dd>
<dt id="OfflineSearchIndex">
/sdk-for-flutter-navigate-search-offlinesearchindex-class
</dt>
<dd>
  Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors.
</dd>
<dt id="OfflineSearchIndexListener">
/sdk-for-flutter-navigate-search-offlinesearchindexlistener-class
</dt>
<dd>
  Abstract class to get updates about progress
of creating persistent map index.
</dd>
<dt id="OfflineSearchIndexOptions">
/sdk-for-flutter-navigate-search-offlinesearchindexoptions-class
</dt>
<dd>
  Options to set indexing for offline search.
</dd>
<dt id="OpeningHours">
/sdk-for-flutter-navigate-search-openinghours-class
</dt>
<dd>
  Represents opening hours information.
</dd>
<dt id="Place">
/sdk-for-flutter-navigate-search-place-class
</dt>
<dd>
  Represents a location object, such as a country, a city, a point of interest (POI) etc.
</dd>
<dt id="PlaceCategory">
/sdk-for-flutter-navigate-search-placecategory-class
</dt>
<dd>
  Represents a category of place with different levels of granularity.
</dd>
<dt id="PlaceChain">
/sdk-for-flutter-navigate-search-placechain-class
</dt>
<dd>
  Parameters related to HERE Places chain system.
</dd>
<dt id="PlaceFilter">
/sdk-for-flutter-navigate-search-placefilter-class
</dt>
<dd>
  The filter options to specify a place.
</dd>
<dt id="PlaceFilterEv">
/sdk-for-flutter-navigate-search-placefilterev-class
</dt>
<dd>
  Constraints that are applicable on the places of category EV station.
</dd>
<dt id="PlaceFoodType">
/sdk-for-flutter-navigate-search-placefoodtype-class
</dt>
<dd>
  Parameters related to HERE Places cuisine system.
</dd>
<dt id="PlaceIdQuery">
/sdk-for-flutter-navigate-search-placeidquery-class
</dt>
<dd>
  The options to specify a Place id query.
</dd>
<dt id="POIPaymentDetails">
/sdk-for-flutter-navigate-search-poipaymentdetails-class
</dt>
<dd>
  Details about the payment options at the POI.
</dd>
<dt id="POIPaymentMethod">
/sdk-for-flutter-navigate-search-poipaymentmethod-class
</dt>
<dd>
  Holds constants that represent payment methods.
</dd>
<dt id="ResponseDetails">
/sdk-for-flutter-navigate-search-responsedetails-class
</dt>
<dd>
  Structure holding various information received with response to a query.
</dd>
<dt id="ScheduleDetails">
/sdk-for-flutter-navigate-search-scheduledetails-class
</dt>
<dd>
  Encapsulates schedule details complying with the iCalendar specification: <a href="https://tools.ietf.org/html/rfc5545">https://tools.ietf.org/html/rfc5545</a>.
</dd>
<dt id="SearchEngine">
/sdk-for-flutter-navigate-search-searchengine-class
</dt>
<dd>
  The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services
to provide developers with unmatched flexibility to create differentiating location-enabled
applications.
</dd>
<dt id="SearchInterface">
/sdk-for-flutter-navigate-search-searchinterface-class
</dt>
<dd>
  Provides the abstract class for the online and offline
search engines.
</dd>
<dt id="SearchOptions">
/sdk-for-flutter-navigate-search-searchoptions-class
</dt>
<dd>
  Encapsulates options that control the behavior of search and suggest operations.
</dd>
<dt id="StructuredQuery">
/sdk-for-flutter-navigate-search-structuredquery-class
</dt>
<dd>
  The options to specify a structured query.
</dd>
<dt id="StructuredQueryAddressElements">
/sdk-for-flutter-navigate-search-structuredqueryaddresselements-class
</dt>
<dd>
  Defines query address elements which will be used to build address hierarchy during searches.
</dd>
<dt id="Suggestion">
/sdk-for-flutter-navigate-search-suggestion-class
</dt>
<dd>
  Suggestion is meant to provide relevant suggestions to partial queries, like "restaur", "starbu", "eiffel".
</dd>
<dt id="SupplierReference">
/sdk-for-flutter-navigate-search-supplierreference-class
</dt>
<dd>
  Identifier of the place as provided by the supplier
</dd>
<dt id="TextQuery">
/sdk-for-flutter-navigate-search-textquery-class
</dt>
<dd>
  The options to specify a text query.
</dd>
<dt id="TextQueryArea">
/sdk-for-flutter-navigate-search-textqueryarea-class
</dt>
<dd>
  Area to perform search on.
</dd>
<dt id="TimeOfDayRange">
/sdk-for-flutter-navigate-search-timeofdayrange-class
</dt>
<dd>
  Time period when the tariff element is valid, in local time.
</dd>
<dt id="TruckAmenities">
/sdk-for-flutter-navigate-search-truckamenities-class
</dt>
<dd>
  Truck amenities struct, represents availability (true/false) for each feature,
except shower_count - number of showers, if data is available.
</dd>
<dt id="TruckFuel">
/sdk-for-flutter-navigate-search-truckfuel-class
</dt>
<dd>
  Contains truck fuel type info of fuel station.
</dd>
<dt id="W3WSearchEngine">
/sdk-for-flutter-navigate-search-w3wsearchengine-class
</dt>
<dd>
  what3words is an alternative geocode system designed to identify any location on the planet.
</dd>
<dt id="W3WSquare">
/sdk-for-flutter-navigate-search-w3wsquare-class
</dt>
<dd>
  Contains information about one of the squares in the what3words geocode system.
</dd>
<dt id="WebDetails">
/sdk-for-flutter-navigate-search-webdetails-class
</dt>
<dd>
  Contains information about images, editorials, rating and a urls to them.
</dd>
<dt id="WebEditorial">
/sdk-for-flutter-navigate-search-webeditorial-class
</dt>
<dd>
  Contains information about editorial article and a link to it.
</dd>
<dt id="WebImage">
/sdk-for-flutter-navigate-search-webimage-class
</dt>
<dd>
  Contains image information and direct link to it.
</dd>
<dt id="WebRating">
/sdk-for-flutter-navigate-search-webrating-class
</dt>
<dd>
  Contains information about rating and a url to review.
</dd>
<dt id="WebsiteAddress">
/sdk-for-flutter-navigate-search-websiteaddress-class
</dt>
<dd>
  Represents data related to specific website address
</dd>
<dt id="WebSource">
/sdk-for-flutter-navigate-search-websource-class
</dt>
<dd>
  Contains information about provider of the item
and a direct link to the item.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="AddressType">
/sdk-for-flutter-navigate-search-addresstype
</dt>
<dd>
  Address type
</dd>
<dt id="AreaType">
/sdk-for-flutter-navigate-search-areatype
</dt>
<dd>
  Represents a type of area like country, state, city, county, etc.
</dd>
<dt id="DayOfWeek">
/sdk-for-flutter-navigate-search-dayofweek
</dt>
<dd>
  Represents the day of the week.
</dd>
<dt id="EnergySourceType">
/sdk-for-flutter-navigate-search-energysourcetype
</dt>
<dd>
  Represents energy source type.
</dd>
<dt id="EnvironmentalImpactCategory">
/sdk-for-flutter-navigate-search-environmentalimpactcategory
</dt>
<dd>
  Represents environmental impacts category of the environmental impact for energy mix.
</dd>
<dt id="EVAccessRestrictionReason">
/sdk-for-flutter-navigate-search-evaccessrestrictionreason
</dt>
<dd>
  Represents the restriction reason of an <code>EVChargingPool</code>.
</dd>
<dt id="EVAccessType">
/sdk-for-flutter-navigate-search-evaccesstype
</dt>
<dd>
  Represents the accessibility level of an <code>EVChargingPool</code>.
</dd>
<dt id="EVChargingLocationFeature">
/sdk-for-flutter-navigate-search-evcharginglocationfeature
</dt>
<dd>
  Optional features that can be requested for EV charging locations.
</dd>
<dt id="EVChargingTariffDimension">
/sdk-for-flutter-navigate-search-evchargingtariffdimension
</dt>
<dd>
  Represents the dimension the price component, which determines what is being charged and how:
</dd>
<dt id="EVChargingTariffType">
/sdk-for-flutter-navigate-search-evchargingtarifftype
</dt>
<dd>
  Represents the tariff pricing model (adhoc, emsp, or cpo).
</dd>
<dt id="EVChargingVehicleCategory">
/sdk-for-flutter-navigate-search-evchargingvehiclecategory
</dt>
<dd>
  Represents the category of the vehicle supported at the charging point.
</dd>
<dt id="EVSearchError">
/sdk-for-flutter-navigate-search-evsearcherror
</dt>
<dd>
  Specifies possible errors that <code>EVSearchEngine</code> may report.
</dd>
<dt id="EVSEStatus">
/sdk-for-flutter-navigate-search-evsestatus
</dt>
<dd>
  EVSE status
</dd>
<dt id="FacilityType">
/sdk-for-flutter-navigate-search-facilitytype
</dt>
<dd>
  Represents facility type available at the location.
</dd>
<dt id="HighlightType">
/sdk-for-flutter-navigate-search-highlighttype
</dt>
<dd>
  Specifies members of Suggestion class to which input query can be matched.
</dd>
<dt id="OfflineSearchIndexError">
/sdk-for-flutter-navigate-search-offlinesearchindexerror
</dt>
<dd>
  Error corresponding to the offline search operation.
</dd>
<dt id="OfflineSearchIndexOperation">
/sdk-for-flutter-navigate-search-offlinesearchindexoperation
</dt>
<dd>
  Shows the operation that is performed over index.
</dd>
<dt id="ParkingType">
/sdk-for-flutter-navigate-search-parkingtype
</dt>
<dd>
  Represents parking type available at the location.
</dd>
<dt id="PlaceSerializationError">
/sdk-for-flutter-navigate-search-placeserializationerror
</dt>
<dd>
  Represents and error, which occurs during place serialization and deserialization routines.
</dd>
<dt id="PlaceType">
/sdk-for-flutter-navigate-search-placetype
</dt>
<dd>
  Specifies place type of Place result from a search query.
</dd>
<dt id="SearchError">
/sdk-for-flutter-navigate-search-searcherror
</dt>
<dd>
  Specifies possible errors that may result from a search query.
</dd>
<dt id="StructuredQueryResultType">
/sdk-for-flutter-navigate-search-structuredqueryresulttype
</dt>
<dd>
  Specifies expected result type.
</dd>
<dt id="SuggestionType">
/sdk-for-flutter-navigate-search-suggestiontype
</dt>
<dd>
  Specifies the type of suggestion returned for query.
</dd>
<dt id="W3WSearchError">
/sdk-for-flutter-navigate-search-w3wsearcherror
</dt>
<dd>
  Specifies possible errors that may result from a w3w search query.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="typedefs">
<h2>Typedefs</h2>
<dl>
<dt class="callable" id="EVSearchCallback">
/sdk-for-flutter-navigate-search-evsearchcallback
= void Function(/sdk-for-flutter-navigate-search-evsearcherror? error, List&lt;<wbr/>/sdk-for-flutter-navigate-search-evcharginglocation-class&gt;? chargingLocations)

</dt>
<dd>
    The method that will be called on the main thread when a search operation in <code>EVSearchEngine</code>
has been completed.
    

  </dd>
<dt class="callable" id="PlaceIdSearchCallback">
/sdk-for-flutter-navigate-search-placeidsearchcallback
= void Function(/sdk-for-flutter-navigate-search-searcherror? searchError, /sdk-for-flutter-navigate-search-place-class? place)

</dt>
<dd>
    The method will be called on the main thread when a search by id call has been completed.
    

  </dd>
<dt class="callable" id="PlaceIdSearchCallbackExtended">
/sdk-for-flutter-navigate-search-placeidsearchcallbackextended
= void Function(/sdk-for-flutter-navigate-search-searcherror? searchError, /sdk-for-flutter-navigate-search-place-class? place, /sdk-for-flutter-navigate-search-responsedetails-class? responseDetails)

</dt>
<dd>
    The method will be called on the main thread when a search by id call has been completed.
    

  </dd>
<dt class="callable" id="SearchCallback">
/sdk-for-flutter-navigate-search-searchcallback
= void Function(/sdk-for-flutter-navigate-search-searcherror? searchError, List&lt;<wbr/>/sdk-for-flutter-navigate-search-place-class&gt;? places)

</dt>
<dd>
    The method will be called on the main thread when a search call has been completed.
    

  </dd>
<dt class="callable" id="SearchCallbackExtended">
/sdk-for-flutter-navigate-search-searchcallbackextended
= void Function(/sdk-for-flutter-navigate-search-searcherror? searchError, List&lt;<wbr/>/sdk-for-flutter-navigate-search-place-class&gt;? places, /sdk-for-flutter-navigate-search-responsedetails-class? responseDetails)

</dt>
<dd>
    The method will be called on the main thread when a search call has been completed.
    

  </dd>
<dt class="callable" id="SuggestCallback">
/sdk-for-flutter-navigate-search-suggestcallback
= void Function(/sdk-for-flutter-navigate-search-searcherror? searchError, List&lt;<wbr/>/sdk-for-flutter-navigate-search-suggestion-class&gt;? suggestions)

</dt>
<dd>
    The method will be called on the main thread when a suggest call has been completed.
    

  </dd>
<dt class="callable" id="SuggestCallbackExtended">
/sdk-for-flutter-navigate-search-suggestcallbackextended
= void Function(/sdk-for-flutter-navigate-search-searcherror? searchError, List&lt;<wbr/>/sdk-for-flutter-navigate-search-suggestion-class&gt;? suggestions, /sdk-for-flutter-navigate-search-responsedetails-class? responseDetails)

</dt>
<dd>
    The method will be called on the main thread when a suggest call has been completed.
    

  </dd>
<dt class="callable" id="W3WSearchCallback">
/sdk-for-flutter-navigate-search-w3wsearchcallback
= void Function(/sdk-for-flutter-navigate-search-w3wsearcherror? searchError, /sdk-for-flutter-navigate-search-w3wsquare-class? square)

</dt>
<dd>
    The method that will be called on the main thread when a search operation in <code>W3WSearchEngine</code>
has been completed.
    

  </dd>
</dl>
</section>
<section class="summary offset-anchor" id="exceptions">
<h2>Exceptions / Errors</h2>
<dl>
<dt id="PlaceSerializationExceptionException">
/sdk-for-flutter-navigate-search-placeserializationexceptionexception-class
</dt>
<dd>
  Place serialization exception
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
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">search.dart</li>
</ol>
<h5>here_sdk package</h5>
<ol>
<li class="section-title">Libraries</li>
<li>/sdk-for-flutter-navigate-animation-animation-library</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-errors-core-errors-library</li>
<li>/sdk-for-flutter-navigate-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-ev-ev-library</li>
<li>/sdk-for-flutter-navigate-gestures-gestures-library</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li>/sdk-for-flutter-navigate-venue-venue-library</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li>/sdk-for-flutter-navigate-venue-style-venue-style-library</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
</ol>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
<h5>search library</h5>
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
