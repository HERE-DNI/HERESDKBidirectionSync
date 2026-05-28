---
title: "VehicleSpecification class"
slug: "sdk-for-flutter-navigate-transport-vehiclespecification-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VehicleSpecification-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="transport/VehicleSpecification-class.html#constructors">Constructors</a></li>
<li><a href="transport/VehicleSpecification/VehicleSpecification.html">VehicleSpecification</a></li>
<li class="section-title">
<a href="transport/VehicleSpecification-class.html#instance-properties">Properties</a>
</li>
<li><a href="transport/VehicleSpecification/axleCount.html">axleCount</a></li>
<li><a href="transport/VehicleSpecification/currentWeightInKilograms.html">currentWeightInKilograms</a></li>
<li><a href="transport/VehicleSpecification/emptyWeightInKilograms.html">emptyWeightInKilograms</a></li>
<li><a href="transport/VehicleSpecification/engineSizeInCubicCentimeters.html">engineSizeInCubicCentimeters</a></li>
<li><a href="transport/VehicleSpecification/grossWeightInKilograms.html">grossWeightInKilograms</a></li>
<li><a href="transport/VehicleSpecification/hashCode.html">hashCode</a></li>
<li><a href="transport/VehicleSpecification/hazardousMaterials.html">hazardousMaterials</a></li>
<li><a href="transport/VehicleSpecification/heightInCentimeters.html">heightInCentimeters</a></li>
<li><a href="transport/VehicleSpecification/isCommercial.html">isCommercial</a></li>
<li><a href="transport/VehicleSpecification/isTruckLight.html">isTruckLight</a></li>
<li><a href="transport/VehicleSpecification/kingpinToRearAxleDistanceInCentimeters.html">kingpinToRearAxleDistanceInCentimeters</a></li>
<li><a href="transport/VehicleSpecification/lastCharacterOfLicensePlate.html">lastCharacterOfLicensePlate</a></li>
<li><a href="transport/VehicleSpecification/lengthInCentimeters.html">lengthInCentimeters</a></li>
<li><a href="transport/VehicleSpecification/occupancy.html">occupancy</a></li>
<li><a href="transport/VehicleSpecification/payloadCapacityInKilograms.html">payloadCapacityInKilograms</a></li>
<li class="inherited"><a href="transport/VehicleSpecification/runtimeType.html">runtimeType</a></li>
<li><a href="transport/VehicleSpecification/tiresCount.html">tiresCount</a></li>
<li><a href="transport/VehicleSpecification/trailerAxleCount.html">trailerAxleCount</a></li>
<li><a href="transport/VehicleSpecification/trailerCount.html">trailerCount</a></li>
<li><a href="transport/VehicleSpecification/truckCategory.html">truckCategory</a></li>
<li><a class="deprecated" href="transport/VehicleSpecification/truckType.html">truckType</a></li>
<li><a href="transport/VehicleSpecification/tunnelCategory.html">tunnelCategory</a></li>
<li><a href="transport/VehicleSpecification/weightPerAxleGroup.html">weightPerAxleGroup</a></li>
<li><a href="transport/VehicleSpecification/weightPerAxleInKilograms.html">weightPerAxleInKilograms</a></li>
<li><a href="transport/VehicleSpecification/widthInCentimeters.html">widthInCentimeters</a></li>
<li class="section-title inherited"><a href="transport/VehicleSpecification-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="transport/VehicleSpecification/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="transport/VehicleSpecification/toString.html">toString</a></li>
<li class="section-title"><a href="transport/VehicleSpecification-class.html#operators">Operators</a></li>
<li><a href="transport/VehicleSpecification/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li class="self-crumb">VehicleSpecification class</li>
</ol>
<div class="self-name">VehicleSpecification</div>
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
<div class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/VehicleSpecification-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VehicleSpecification class</h1></div>
<section class="desc markdown">
<p>Contains vehicle related attributes.</p>
<p>Examples: Dimensions, weight, axle count.
Only the fields that are set are considered for restriction handling.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VehicleSpecification">
/sdk-for-flutter-navigate-transport-vehiclespecification-vehiclespecification()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="axleCount">
/sdk-for-flutter-navigate-transport-vehiclespecification-axlecount
↔ int?
</dt>
<dd>
  Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2.
By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be taken into consideration.
Rendering: When set, truck restriction icons for an axle count greater than /sdk-for-flutter-navigate-transport-vehiclespecification-axlecount will not be displayed.
When specifying /sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount, then /sdk-for-flutter-navigate-transport-vehiclespecification-axlecount is required and must be greater than /sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="currentWeightInKilograms">
/sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms
↔ int?
</dt>
<dd>
  Current truck weight, including trailers and shipped goods currently loaded, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to /sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="emptyWeightInKilograms">
/sdk-for-flutter-navigate-transport-vehiclespecification-emptyweightinkilograms
↔ int?
</dt>
<dd>
  Empty weight of the vehicle without any load, excluding trailers, specified in kilograms.
The provided value must be greater than or equal to 0.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="engineSizeInCubicCentimeters">
/sdk-for-flutter-navigate-transport-vehiclespecification-enginesizeincubiccentimeters
↔ int?
</dt>
<dd>
  Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535.
Default value is <code>null</code>, which means the scooter route calculation ignores all engine size limits on the
road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="grossWeightInKilograms">
/sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms
↔ int?
</dt>
<dd>
  Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to /sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-transport-vehiclespecification-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="hazardousMaterials">
/sdk-for-flutter-navigate-transport-vehiclespecification-hazardousmaterials
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-transport-hazardousmaterial&gt;
</dt>
<dd>
  Specifies a list of hazardous materials shipped in the vehicle.
Refer to /sdk-for-flutter-navigate-transport-hazardousmaterial for the available options.
By default, it is an empty list.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="heightInCentimeters">
/sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters
↔ int?
</dt>
<dd>
  Vehicle height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isCommercial">
/sdk-for-flutter-navigate-transport-vehiclespecification-iscommercial
↔ bool
</dt>
<dd>
  Specifies whether the vehicle is a commercial or a non-commercial vehicle.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTruckLight">
/sdk-for-flutter-navigate-transport-vehiclespecification-istrucklight
↔ bool
</dt>
<dd>
  A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
The flag should not be set to <code>true</code> in other countries than Japan.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="kingpinToRearAxleDistanceInCentimeters">
/sdk-for-flutter-navigate-transport-vehiclespecification-kingpintorearaxledistanceincentimeters
↔ int?
</dt>
<dd>
  Defines the kingpin to rear axle distance, in centimeters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lastCharacterOfLicensePlate">
/sdk-for-flutter-navigate-transport-vehiclespecification-lastcharacteroflicenseplate
↔ String?
</dt>
<dd>
  Last character of license plate in String format. This value can be used to
evaluate restrictions in environmental zones.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lengthInCentimeters">
/sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters
↔ int?
</dt>
<dd>
  Vehicle length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="occupancy">
/sdk-for-flutter-navigate-transport-vehiclespecification-occupancy
↔ int?
</dt>
<dd>
  Specifies the number of occupants in the vehicle, including driver,
can affect the vehicle's ability to use HOV/carpool restricted lanes.
Should not be less than 1 or greater than 255.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="payloadCapacityInKilograms">
/sdk-for-flutter-navigate-transport-vehiclespecification-payloadcapacityinkilograms
↔ int?
</dt>
<dd>
  Allowed payload capacity, including trailers, specified in kilograms. The provided value
must be greater then or equal to 0.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-transport-vehiclespecification-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tiresCount">
/sdk-for-flutter-navigate-transport-vehiclespecification-tirescount
↔ int?
</dt>
<dd>
  The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers.
By default, it is not set.
Otherwise it is guaranteed to be in the range [1, 255].
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trailerAxleCount">
/sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount
↔ int?
</dt>
<dd>
  Defines total number of axles across all the trailers attached to the vehicle.
This number is included in /sdk-for-flutter-navigate-transport-vehiclespecification-axlecount, hence /sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount must be less than /sdk-for-flutter-navigate-transport-vehiclespecification-axlecount
and greater than or equal to 1. /sdk-for-flutter-navigate-transport-vehiclespecification-axlecount and /sdk-for-flutter-navigate-transport-vehiclespecification-trailercount are required to specify /sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trailerCount">
/sdk-for-flutter-navigate-transport-vehiclespecification-trailercount
↔ int?
</dt>
<dd>
  Defines number of trailers attached to the vehicle. The provided value must be in the range [0, 255].
By default, it is not set.
When specifying /sdk-for-flutter-navigate-transport-vehiclespecification-traileraxlecount, then /sdk-for-flutter-navigate-transport-vehiclespecification-trailercount is required and must be greater than 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckCategory">
/sdk-for-flutter-navigate-transport-vehiclespecification-truckcategory
↔ /sdk-for-flutter-navigate-transport-truckcategory?
</dt>
<dd>
  Defines the truck category.
By default, it is not set.
Rendering: /sdk-for-flutter-navigate-transport-vehiclespecification-truckcategory is ignored and has no effect.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckType">
/sdk-for-flutter-navigate-transport-vehiclespecification-trucktype
↔ /sdk-for-flutter-navigate-transport-trucktype
</dt>
<dd>
  Will be replaced with <code>truckCategory</code> when the <code>TruckSpecification</code> will be replaced by <code>VehicleSpecification</code>.
Defines the type of truck.
Defaults to /sdk-for-flutter-navigate-transport-trucktype.
Rendering <code>sdk.mapview.TruckProfile</code>: /sdk-for-flutter-navigate-transport-vehiclespecification-trucktype is ignored and has no effect.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tunnelCategory">
/sdk-for-flutter-navigate-transport-vehiclespecification-tunnelcategory
↔ /sdk-for-flutter-navigate-transport-tunnelcategory?
</dt>
<dd>
  Specifies the tunnel categories to restrict certain route links.
The route will pass only through tunnels of a less strict category.
Refer to /sdk-for-flutter-navigate-transport-tunnelcategory for the available options.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="weightPerAxleGroup">
/sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxlegroup
↔ /sdk-for-flutter-navigate-transport-weightperaxlegroup-class?
</dt>
<dd>
  Allows specification of axle weights in a more fine-grained way than /sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxleinkilograms.
This is relevant in countries with signs and regulations that specify different limits for different axle
groups, like the USA and Sweden.
By default is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="weightPerAxleInKilograms">
/sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxleinkilograms
↔ int?
</dt>
<dd>
  Heaviest weight per axle, regardless of axle type or axle group.
It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
The provided value must be greater or equal to 0.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="widthInCentimeters">
/sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters
↔ int?
</dt>
<dd>
  Vehicle width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-transport-vehiclespecification-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-transport-vehiclespecification-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-navigate-transport-vehiclespecification-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li class="self-crumb">VehicleSpecification class</li>
</ol>
<h5>transport library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
