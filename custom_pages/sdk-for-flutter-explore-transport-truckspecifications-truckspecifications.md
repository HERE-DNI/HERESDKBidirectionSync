---
title: "TruckSpecifications constructor"
slug: "sdk-for-flutter-explore-transport-truckspecifications-truckspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TruckSpecifications.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-transport-transport-library</li>
<li>/sdk-for-flutter-explore-transport-truckspecifications-class</li>
<li class="self-crumb">TruckSpecifications constructor</li>
</ol>
<div class="self-name">TruckSpecifications</div>
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
<div class="main-content" data-above-sidebar="transport/TruckSpecifications-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>TruckSpecifications constructor</h1></div>
<section class="multi-line-signature">
TruckSpecifications(<wbr/>[<ol class="parameter-list"> <li>int? grossWeightInKilograms = null, </li>
<li>int? currentWeightInKilograms = null, </li>
<li>int? weightPerAxleInKilograms = null, </li>
<li>/sdk-for-flutter-explore-transport-weightperaxlegroup-class? weightPerAxleGroup = null, </li>
<li>int? heightInCentimeters = null, </li>
<li>int? widthInCentimeters = null, </li>
<li>int? lengthInCentimeters = null, </li>
<li>int? axleCount = null, </li>
<li>int? trailerCount = null, </li>
<li>/sdk-for-flutter-explore-transport-trucktype truckType = TruckType.straight, </li>
<li>bool isTruckLight = false, </li>
<li>int? payloadCapacityInKilograms = null, </li>
<li>int? trailerAxleCount = null, </li>
</ol>])
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>grossWeightInKilograms</code> Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to /sdk-for-flutter-explore-transport-truckspecifications-currentweightinkilograms. By default, it is not set.</li>
<li><code>currentWeightInKilograms</code> Current truck weight, including trailers and shipped goods currently loaded, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to /sdk-for-flutter-explore-transport-truckspecifications-grossweightinkilograms. By default, it is not set.</li>
<li><code>weightPerAxleInKilograms</code> Heaviest weight per axle, regardless of axle type or axle group.
It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
The provided value must be greater or equal to 0.
By default, it is not set.
<strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
When available for your edition, if both attributes are set, during online RoutingEngine an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.
Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</li>
<li><code>weightPerAxleGroup</code> Allows specification of axle weights in a more fine-grained way than <code>weight_per_axle_in_kilograms</code>.
This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden.
By default is not set.
<strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
When available for your edition, if both attributes are set, during online RoutingEngine an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.
Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</li>
<li><code>heightInCentimeters</code> Truck height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
<li><code>widthInCentimeters</code> Truck width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
<li><code>lengthInCentimeters</code> Truck length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.</li>
<li><code>axleCount</code> Defines total number of axles in the vehicle. The provided value must be greater than or
equal to 2. By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be
taken into consideration.
Rendering <code>sdk.mapview.TruckProfile</code>: When set, truck restriction icons for an axle count
greater than /sdk-for-flutter-explore-transport-truckspecifications-axlecount will not be displayed.
When specifying /sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount, then /sdk-for-flutter-explore-transport-truckspecifications-axlecount is required and must be greater than /sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount.</li>
<li><code>trailerCount</code> Defines number of trailers attached to the vehicle. The provided value must be in the range
[0, 255]. By default, it is not set.
When specifying /sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount, then /sdk-for-flutter-explore-transport-truckspecifications-trailercount is required and must be greater than 0.</li>
<li><code>truckType</code> Defines the type of truck. By default, it is /sdk-for-flutter-explore-transport-trucktype.
Rendering <code>sdk.mapview.TruckProfile</code>: /sdk-for-flutter-explore-transport-truckspecifications-trucktype is ignored and has no effect.</li>
<li><code>isTruckLight</code> A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
The flag should not be set to <code>true</code> in other countries than Japan. The flag defaults to <code>false</code>.</li>
</ul>
<p>A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets
the vehicle can access, which access restrictions apply, and which speed limits are applicable.
Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will
not always overwrite these settings: Make sure to not exceed the specifications that classify a truck as light.</p>
<p>In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to true,
you will get, for example, the same speed limits as for cars. Make sure to set the flag only to true, when
a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.</p>
<p>When <code>TruckSpecifications</code> are set as part of <code>MapContentSettings</code>, then this flag will be ignored and
has no effect.</p>
<p><strong>Note:</strong>
This flag and the concept of light trucks are supported only in Japan as beta and are considered to be
experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.
Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases with a deprecation process.</p>
<ul>
<li><code>payloadCapacityInKilograms</code> Allowed payload capacity, including trailers, specified in kilograms. The provided value
must be greater then or equal to 0. By default, it is not set.</li>
<li><code>trailerAxleCount</code> Defines total number of axles across all the trailers attached to the vehicle.
This number is included in /sdk-for-flutter-explore-transport-truckspecifications-axlecount, hence /sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount must be less than /sdk-for-flutter-explore-transport-truckspecifications-axlecount
and greater than or equal to 1. /sdk-for-flutter-explore-transport-truckspecifications-axlecount and /sdk-for-flutter-explore-transport-truckspecifications-trailercount are required to specify /sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount.
By default, it is not set.
Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TruckSpecifications([int? grossWeightInKilograms = null, int? currentWeightInKilograms = null, int? weightPerAxleInKilograms = null, WeightPerAxleGroup? weightPerAxleGroup = null, int? heightInCentimeters = null, int? widthInCentimeters = null, int? lengthInCentimeters = null, int? axleCount = null, int? trailerCount = null, TruckType truckType = TruckType.straight, bool isTruckLight = false, int? payloadCapacityInKilograms = null, int? trailerAxleCount = null])
  : grossWeightInKilograms = grossWeightInKilograms, currentWeightInKilograms = currentWeightInKilograms, weightPerAxleInKilograms = weightPerAxleInKilograms, weightPerAxleGroup = weightPerAxleGroup ?? null, heightInCentimeters = heightInCentimeters, widthInCentimeters = widthInCentimeters, lengthInCentimeters = lengthInCentimeters, axleCount = axleCount, trailerCount = trailerCount, truckType = truckType, isTruckLight = isTruckLight, payloadCapacityInKilograms = payloadCapacityInKilograms, trailerAxleCount = trailerAxleCount;</code></pre>
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
<li>/sdk-for-flutter-explore-transport-transport-library</li>
<li>/sdk-for-flutter-explore-transport-truckspecifications-class</li>
<li class="self-crumb">TruckSpecifications constructor</li>
</ol>
<h5>TruckSpecifications class</h5>
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
