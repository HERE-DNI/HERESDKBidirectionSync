---
title: "Untitled"
slug: "sdk-for-flutter-navigate-transport-vehiclerestriction-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VehicleRestriction-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li class="self-crumb">VehicleRestriction class</li>
</ol>
<div class="self-name">VehicleRestriction</div>
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
<div class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/VehicleRestriction-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VehicleRestriction class</h1></div>
<section class="desc markdown">
<p>Represents a vehicle restriction.</p>
<p>Any non <code>null</code> property adds more details to the restriction.
A general truck restriction is represented with <code>null</code> values for
properties <code>restriction</code> and
<code>hazmatRestriction</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VehicleRestriction">
/sdk-for-flutter-navigate-transport-vehiclerestriction-vehiclerestriction(/sdk-for-flutter-navigate-transport-specificrestriction-class? restriction)
</dt>
<dd>
          Creates an unconditional restriction.
        </dd>
<dt class="callable" id="VehicleRestriction.generalRestriction">
/sdk-for-flutter-navigate-transport-vehiclerestriction-vehiclerestriction-generalrestriction()
</dt>
<dd>
          Creates an uncoditional general restriction.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="appliesToDelivery">
/sdk-for-flutter-navigate-transport-vehiclerestriction-appliestodelivery
↔ bool
</dt>
<dd>
  Flag indicating whether this restriction applies to delivery vehicles.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="axleCount">
/sdk-for-flutter-navigate-transport-vehiclerestriction-axlecount
↔ /sdk-for-flutter-navigate-core-integerrange-class?
</dt>
<dd>
  The axle count for which the current restriction applies.
Can be used in conjunction with /sdk-for-flutter-navigate-transport-restrictiontype
to specify restriction based on weight per number of axles.
The <code>axleCount</code> considers total number of axles on the whole vehicle (truck + trailers).
This can be used to limit the weight per axle for the whole truck.
If <code>axleCount</code> is null, the restriction is general and applies regardless of axle count.
If the upper limit of the <code>axleCount</code> range is 0 or <code>null</code> then it means the restriction applies
for values &gt;= lower limit, i.e. the upper limit of range if infinite or unbound.
When a user taps the icon, the allowed <code>axleCount</code> range can be retrieved directly
from <code>VehicleRestriction.axleCount</code>.
Examples:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="axleCountInGroup">
/sdk-for-flutter-navigate-transport-vehiclerestriction-axlecountingroup
↔ /sdk-for-flutter-navigate-core-integerrange-class?
</dt>
<dd>
  Number of axles in a group for which the current restriction applies.
<code>axleCountInGroup</code> is a set of axles close together: single, tandem (2), triple (3), etc.
Can be used in conjunction with /sdk-for-flutter-navigate-transport-restrictiontype
to specify restriction based on weight per axle group.
The <code>axleCountInGroup</code> considers number of axles in a specific axle group (usually rear axles on the truck or trailer).
This can be used to limit weight for a tandem/triple rear axle group.
If the upper limit of the <code>axleCountInGroup</code> range is 0 or <code>null</code> then it means the restriction applies
for values &gt;= lower limit, i.e. the upper limit of range if infinite or unbound.
Examples:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-transport-vehiclerestriction-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="hazmatRestriction">
/sdk-for-flutter-navigate-transport-vehiclerestriction-hazmatrestriction
↔ /sdk-for-flutter-navigate-transport-hazardousmaterialrestriction-class?
</dt>
<dd>
  Restriction on transport of hazardous materials and max allowed tunnel category.
For example, (FLAMMABLE, TunnelCategory.D) means, a restriction applying for trucks
carrying flammable materials are not allowed to enter tunnels category D and E -
(TunnelCategory.B and TunnelCategory.C allowed).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="restriction">
/sdk-for-flutter-navigate-transport-vehiclerestriction-restriction
↔ /sdk-for-flutter-navigate-transport-specificrestriction-class?
</dt>
<dd>
  A <code>SpecificRestriction</code> defines what type of restriction applies (weight, height, etc.)
and the range of allowed values.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-transport-vehiclerestriction-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="timeRestriction">
/sdk-for-flutter-navigate-transport-vehiclerestriction-timerestriction
↔ /sdk-for-flutter-navigate-transport-timerestriction-class?
</dt>
<dd>
  Restriction applies during specific time.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trailerCount">
/sdk-for-flutter-navigate-transport-vehiclerestriction-trailercount
↔ /sdk-for-flutter-navigate-core-integerrange-class?
</dt>
<dd>
  Number of trailers for which the restriction applies.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckCategory">
/sdk-for-flutter-navigate-transport-vehiclerestriction-truckcategory
↔ /sdk-for-flutter-navigate-transport-truckcategory?
</dt>
<dd>
  Restriction applies to a specific truck category.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="weather">
/sdk-for-flutter-navigate-transport-vehiclerestriction-weather
↔ /sdk-for-flutter-navigate-navigation-weathertype?
</dt>
<dd>
  Type of weather in which restriction applies.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-transport-vehiclerestriction-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-transport-vehiclerestriction-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-transport-vehiclerestriction-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">VehicleRestriction class</li>
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



</div>
`
}</HTMLBlock>
