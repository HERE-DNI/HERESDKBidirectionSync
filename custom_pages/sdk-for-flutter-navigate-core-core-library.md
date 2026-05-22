---
title: "Untitled"
slug: "sdk-for-flutter-navigate-core-core-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- core-library.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">core.dart</li>
</ol>
<div class="self-name">core</div>
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
<div class="main-content" data-above-sidebar="" data-below-sidebar="core/core-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>core library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="Anchor2D">
/sdk-for-flutter-navigate-core-anchor2d-class
</dt>
<dd>
  Represents a point in a rectangle as a ratio of this rectangle's width and height.
</dd>
<dt id="Angle">
/sdk-for-flutter-navigate-core-angle-class
</dt>
<dd>
  Represents an angle independent of the unit of measurement.
</dd>
<dt id="AngleRange">
/sdk-for-flutter-navigate-core-anglerange-class
</dt>
<dd>
  Represents angle ranges as a circular sector by using an absolute start angle
and a relative range angle called extent.
</dd>
<dt id="Authentication">
/sdk-for-flutter-navigate-core-authentication-class
</dt>
<dd>
  Use the authentication class to authenticate and retrieve a secure token that
can be used with other HERE services.
</dd>
<dt id="AuthenticationData">
/sdk-for-flutter-navigate-core-authenticationdata-class
</dt>
<dd>
  Authentication data
</dd>
<dt id="BrandLogo">
/sdk-for-flutter-navigate-core-brandlogo-class
</dt>
<dd>
  Represents image link to the company's logo.
</dd>
<dt id="CustomMetadataValue">
/sdk-for-flutter-navigate-core-custommetadatavalue-class
</dt>
<dd>
  Abstract class for storing arbitrary metadata types.
</dd>
<dt id="ExternalID">
/sdk-for-flutter-navigate-core-externalid-class
</dt>
<dd>
  Identifier of the entity as provided by the external source
</dd>
<dt id="GeoBox">
/sdk-for-flutter-navigate-core-geobox-class
</dt>
<dd>
  Represents a bounding rectangle aligned with latitude and longitude.
</dd>
<dt id="GeoCircle">
/sdk-for-flutter-navigate-core-geocircle-class
</dt>
<dd>
  Represents a circle area in 2D space.
</dd>
<dt id="GeoCoordinates">
/sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  Represents geographical coordinates in 3D space.
</dd>
<dt id="GeoCoordinatesUpdate">
/sdk-for-flutter-navigate-core-geocoordinatesupdate-class
</dt>
<dd>
  Represents geographical coordinates in 3D space.
</dd>
<dt id="GeoCorridor">
/sdk-for-flutter-navigate-core-geocorridor-class
</dt>
<dd>
  A geographical area that wraps around a geographical polyline with a given distance.
</dd>
<dt id="GeoOrientation">
/sdk-for-flutter-navigate-core-geoorientation-class
</dt>
<dd>
  Geodetic orientation with bearing, tilt and roll.
</dd>
<dt id="GeoOrientationUpdate">
/sdk-for-flutter-navigate-core-geoorientationupdate-class
</dt>
<dd>
  Describes geodetic orientation update with bearing and tilt.
</dd>
<dt id="GeoPolygon">
/sdk-for-flutter-navigate-core-geopolygon-class
</dt>
<dd>
  Represents a <code>GeoPolygon</code> area as a series of geographic coordinates, and optionally,
a list of inner boundaries (also known as holes).
</dd>
<dt id="GeoPolyline">
/sdk-for-flutter-navigate-core-geopolyline-class
</dt>
<dd>
  A list of geographic coordinates representing the vertices of a polyline.
</dd>
<dt id="IntegerRange">
/sdk-for-flutter-navigate-core-integerrange-class
</dt>
<dd>
  An integer range [min, max] with inclusive minimum and maximum value.
</dd>
<dt id="LocalizedText">
/sdk-for-flutter-navigate-core-localizedtext-class
</dt>
<dd>
  Used to represent text localized to specific language.
</dd>
<dt id="LocalizedTexts">
/sdk-for-flutter-navigate-core-localizedtexts-class
</dt>
<dd>
  The list of multiple names or titles for the same entity, possibly in different languages.
</dd>
<dt id="Location">
/sdk-for-flutter-navigate-core-location-class
</dt>
<dd>
  Describes a location in the world at a given time.
</dd>
<dt id="LocationListener">
/sdk-for-flutter-navigate-core-locationlistener-class
</dt>
<dd>
  This abstract class should be implemented in order to receive notifications
about location updates.
</dd>
<dt id="LocationTime">
/sdk-for-flutter-navigate-core-locationtime-class
</dt>
<dd>
  This struct presents all the time data tied to a location, like an arrival or departure time.
</dd>
<dt id="Metadata">
/sdk-for-flutter-navigate-core-metadata-class
</dt>
<dd>
  Holds metadata on behalf of a map item.
</dd>
<dt id="NameID">
/sdk-for-flutter-navigate-core-nameid-class
</dt>
<dd>
  Structure to represent name-id pairs.
</dd>
<dt id="NetworkEndpoint">
/sdk-for-flutter-navigate-core-networkendpoint-class
</dt>
<dd>
  Network endpoint.
</dd>
<dt id="ParameterConfiguration">
/sdk-for-flutter-navigate-core-parameterconfiguration-class
</dt>
<dd>
  Contains values of configurable parameters that are used in SDK.
</dd>
<dt id="PedestrianProfile">
/sdk-for-flutter-navigate-core-pedestrianprofile-class
</dt>
<dd>
  Contains values of pedestrian profile.
</dd>
<dt id="PickedPlace">
/sdk-for-flutter-navigate-core-pickedplace-class
</dt>
<dd>
  Carries the result of picking a Carto POI (point of interest) object.
</dd>
<dt id="Point2D">
/sdk-for-flutter-navigate-core-point2d-class
</dt>
<dd>
  Represents a point in 2D space.
</dd>
<dt id="Point3D">
/sdk-for-flutter-navigate-core-point3d-class
</dt>
<dd>
  Represents a point in 3D space.
</dd>
<dt id="PolylineSimplifier">
/sdk-for-flutter-navigate-core-polylinesimplifier-class
</dt>
<dd>
  PolylineSimplifier helps to reduce the number of points
in the polyline by removing redundant elements using
Douglas–Peucker algorithm, so that result stays
within /sdk-for-flutter-navigate-core-polylinesimplifieroptions-class.
</dd>
<dt id="PolylineSimplifierOptions">
/sdk-for-flutter-navigate-core-polylinesimplifieroptions-class
</dt>
<dd>
  Controls the strategy of /sdk-for-flutter-navigate-core-polylinesimplifier-simplify
when reducing a size of polyline.
</dd>
<dt id="Rectangle2D">
/sdk-for-flutter-navigate-core-rectangle2d-class
</dt>
<dd>
  Represents a 2D rectangle defined by the origin and size.
</dd>
<dt id="SdkContext">
/sdk-for-flutter-navigate-core-sdkcontext-class
</dt>
<dd>
</dd>
<dt id="Size2D">
/sdk-for-flutter-navigate-core-size2d-class
</dt>
<dd>
  Represents the size of a 2D structure.
</dd>
<dt id="TimeRule">
/sdk-for-flutter-navigate-core-timerule-class
</dt>
<dd>
  Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification.
</dd>
<dt id="TransportProfile">
/sdk-for-flutter-navigate-core-transportprofile-class
</dt>
<dd>
  Contains values of transport profile.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="AuthenticationError">
/sdk-for-flutter-navigate-core-authenticationerror
</dt>
<dd>
  Authentication error
</dd>
<dt id="CardinalDirection">
/sdk-for-flutter-navigate-core-cardinaldirection
</dt>
<dd>
  Indicates the official directional identifier assigned to this road.
</dd>
<dt id="CountryCode">
/sdk-for-flutter-navigate-core-countrycode
</dt>
<dd>
  This enum represents country codes in accordance with the ISO 3166-1 standard using alpha-3 codes.
</dd>
<dt id="CurrentType">
/sdk-for-flutter-navigate-core-currenttype
</dt>
<dd>
  This enum represents the type of electric current
</dd>
<dt id="GeoPolylineDirection">
/sdk-for-flutter-navigate-core-geopolylinedirection
</dt>
<dd>
  Defines if a function on a /sdk-for-flutter-navigate-core-geopolyline-class computes the operation starting from the beginning or
from the end of /sdk-for-flutter-navigate-core-geopolyline-vertices.
</dd>
<dt id="IsolateOrigin">
/sdk-for-flutter-navigate-core-isolateorigin
</dt>
<dd>
</dd>
<dt id="LanguageCode">
/sdk-for-flutter-navigate-core-languagecode
</dt>
<dd>
  This enum represents language codes.
</dd>
<dt id="LocationSource">
/sdk-for-flutter-navigate-core-locationsource
</dt>
<dd>
  Indicates where the location was computed.
</dd>
<dt id="LocationTechnology">
/sdk-for-flutter-navigate-core-locationtechnology
</dt>
<dd>
  Technology or provider of the location.
</dd>
<dt id="MetadataType">
/sdk-for-flutter-navigate-core-metadatatype
</dt>
<dd>
  Different types of objects that can be stored in a Metadata class instance.
</dd>
<dt id="PolylineSimplificationError">
/sdk-for-flutter-navigate-core-polylinesimplificationerror
</dt>
<dd>
  Error code which specifies, what went wrong during
/sdk-for-flutter-navigate-core-polylinesimplifier-simplify operation.
</dd>
<dt id="PowerType">
/sdk-for-flutter-navigate-core-powertype
</dt>
<dd>
  Represents the type of electrical power.
</dd>
<dt id="RouteType">
/sdk-for-flutter-navigate-core-routetype
</dt>
<dd>
  Indicates the level of significance of a route in a range from 1 to 6.
</dd>
<dt id="UnitSystem">
/sdk-for-flutter-navigate-core-unitsystem
</dt>
<dd>
  Represents the available unit systems(imperial/metric).
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="typedefs">
<h2>Typedefs</h2>
<dl>
<dt class="callable" id="AuthenticationCallback">
/sdk-for-flutter-navigate-core-authenticationcallback
= void Function(/sdk-for-flutter-navigate-core-authenticationerror? authenticationError, /sdk-for-flutter-navigate-core-authenticationdata-class? authenticationData)

</dt>
<dd>
    Callback passed to /sdk-for-flutter-navigate-core-authentication-authenticatewithsdknativeengine.
    

  </dd>
<dt class="callable" id="PolylineSimplificationCallback">
/sdk-for-flutter-navigate-core-polylinesimplificationcallback
= void Function(/sdk-for-flutter-navigate-core-polylinesimplificationerror? queryError, List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt;? result)

</dt>
<dd>
    The method will be called on the main thread when
/sdk-for-flutter-navigate-core-polylinesimplifier-simplify is finished.
    

  </dd>
</dl>
</section>
<section class="summary offset-anchor" id="exceptions">
<h2>Exceptions / Errors</h2>
<dl>
<dt id="AuthenticationExceptionException">
/sdk-for-flutter-navigate-core-authenticationexceptionexception-class
</dt>
<dd>
  Authentication exception
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
<li class="self-crumb">core.dart</li>
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
<h5>core library</h5>
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
