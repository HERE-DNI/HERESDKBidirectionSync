---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-truckrestrictionwarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TruckRestrictionWarning-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">TruckRestrictionWarning class</li>
</ol>
<div class="self-name">TruckRestrictionWarning</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TruckRestrictionWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TruckRestrictionWarning class</h1></div>
<section class="desc markdown">
<p>Represents truck restrictions.</p>
<p>For example, there can be a bridge ahead not high enough to pass a big truck
or there can be a road ahead where the truck’s weight exceeds the permissible limit.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TruckRestrictionWarning">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-truckrestrictionwarning(double distanceInMeters, /sdk-for-flutter-navigate-navigation-distancetype distanceType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="axleCount">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-axlecount
↔ /sdk-for-flutter-navigate-core-integerrange-class?
</dt>
<dd>
  The axle count for which the current restriction applies.
If this field is <code>null</code>, the restriction does not depend on axle count.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="dimensionRestriction">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-dimensionrestriction
↔ /sdk-for-flutter-navigate-navigation-dimensionrestriction-class?
</dt>
<dd>
  Vehicle dimension restrictions.
It is <code>null</code> when there is no known dimension restriction ahead.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceInMeters">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distanceinmeters
↔ double
</dt>
<dd>
  The distance from the current location to the restriction.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  Indicates if the specified truck restriction is ahead of the vehicle or has just passed by. If it is ahead, then /sdk-for-flutter-navigate-navigation-truckrestrictionwarning-distanceinmeters is greater than 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="hazardousMaterials">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-hazardousmaterials
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-transport-hazardousmaterial&gt;
</dt>
<dd>
  The list of hazardous materials which are restricted on the road section for which the warning applies.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-id
↔ int
</dt>
<dd>
  Unique identifier for this specific truck restriction warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="timeRule">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-timerule
↔ /sdk-for-flutter-navigate-core-timerule-class?
</dt>
<dd>
  Time rule indicating the time periods for which the restriction applies.
If the field is 'null' then the restriction is applicable at anytime.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trailerCount">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-trailercount
↔ /sdk-for-flutter-navigate-core-integerrange-class?
</dt>
<dd>
  The trailer count for which the current restriction applies.
If the field is 'null' then the current restriction does not have a condition based on trailers count.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckRoadType">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-truckroadtype
↔ /sdk-for-flutter-navigate-transport-truckroadtype?
</dt>
<dd>
  Truck road type restriction.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tunnelCategory">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-tunnelcategory
↔ /sdk-for-flutter-navigate-transport-tunnelcategory?
</dt>
<dd>
  Tunnel category.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="weightRestriction">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-weightrestriction
↔ /sdk-for-flutter-navigate-navigation-weightrestriction-class?
</dt>
<dd>
  Weight restriction.
It is <code>null</code> when there is no known weight restriction ahead.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="isGeneral">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-isgeneral(<wbr/>)
    → bool

</dt>
<dd>
  Checks if this truck restriction warning is general.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">TruckRestrictionWarning class</li>
</ol>
<h5>navigation library</h5>
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
