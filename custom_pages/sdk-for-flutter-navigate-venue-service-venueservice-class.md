---
title: "VenueService class abstract"
slug: "sdk-for-flutter-navigate-venue-service-venueservice-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueService-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="venue.service/VenueService-class.html#constructors">Constructors</a></li>
<li><a href="venue.service/VenueService/VenueService.html">VenueService</a></li>
<li class="section-title">
<a href="venue.service/VenueService-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="venue.service/VenueService/hashCode.html">hashCode</a></li>
<li><a href="venue.service/VenueService/language.html">language</a></li>
<li><a href="venue.service/VenueService/languages.html">languages</a></li>
<li class="inherited"><a href="venue.service/VenueService/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="venue.service/VenueService-class.html#instance-methods">Methods</a></li>
<li><a href="venue.service/VenueService/addServiceListener.html">addServiceListener</a></li>
<li><a href="venue.service/VenueService/addVenueListener.html">addVenueListener</a></li>
<li><a href="venue.service/VenueService/addVenueMapListener.html">addVenueMapListener</a></li>
<li><a href="venue.service/VenueService/addVenueToLoad.html">addVenueToLoad</a></li>
<li><a href="venue.service/VenueService/addVenueToLoadStr.html">addVenueToLoadStr</a></li>
<li><a href="venue.service/VenueService/getInitStatus.html">getInitStatus</a></li>
<li><a href="venue.service/VenueService/isInitialized.html">isInitialized</a></li>
<li><a href="venue.service/VenueService/loadOptionalFeatures.html">loadOptionalFeatures</a></li>
<li><a href="venue.service/VenueService/loadTopologies.html">loadTopologies</a></li>
<li class="inherited"><a href="venue.service/VenueService/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="venue.service/VenueService/removeServiceListener.html">removeServiceListener</a></li>
<li><a href="venue.service/VenueService/removeVenueListener.html">removeVenueListener</a></li>
<li><a href="venue.service/VenueService/removeVenueMapListener.html">removeVenueMapListener</a></li>
<li><a href="venue.service/VenueService/setHrn.html">setHrn</a></li>
<li><a href="venue.service/VenueService/setLabeltextPreference.html">setLabeltextPreference</a></li>
<li><a href="venue.service/VenueService/stop.html">stop</a></li>
<li class="inherited"><a href="venue.service/VenueService/toString.html">toString</a></li>
<li class="section-title inherited"><a href="venue.service/VenueService-class.html#operators">Operators</a></li>
<li class="inherited"><a href="venue.service/VenueService/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li class="self-crumb">VenueService class</li>
</ol>
<div class="self-name">VenueService</div>
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
<div class="main-content" data-above-sidebar="venue.service/venue.service-library-sidebar.html" data-below-sidebar="venue.service/VenueService-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VenueService class abstract</h1></div>
<section class="desc markdown">
<p>Offers methods to download venues.</p>
<p>Use of this
object does not necessitate Map involvement.</p>
<p>
Before loading the venues, initialize the venue service
with one of the start methods.
</p>
<p>
The venue service is online only. Even if there is a cached
venue on the device, the venue service requires an online
connection to check if the venue is available for the user.
</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VenueService">
/sdk-for-flutter-navigate-venue-service-venueservice-venueservice()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-venue-service-venueservice-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="language">
/sdk-for-flutter-navigate-venue-service-venueservice-language
↔ String
</dt>
<dd>
  The active language.
The venue service will try to load
a venue with a translation in the active language. If such translation doesn't
exist, a venue will be loaded in its default language.
Gets an active language in the venue service.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="languages">
/sdk-for-flutter-navigate-venue-service-venueservice-languages
→ /sdk-for-flutter-navigate-venue-service-venueservicestringarray
</dt>
<dd>
  The languages available in the venue service.
Gets the languages available in the venue service.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-service-venueservice-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addServiceListener">
/sdk-for-flutter-navigate-venue-service-venueservice-addservicelistener(<wbr/>/sdk-for-flutter-navigate-venue-service-venueservicelistener-class listener)
    → void

</dt>
<dd>
  Adds a service .
  

</dd>
<dt class="callable" id="addVenueListener">
/sdk-for-flutter-navigate-venue-service-venueservice-addvenuelistener(<wbr/>/sdk-for-flutter-navigate-venue-service-venuelistener-class listener)
    → void

</dt>
<dd>
  Adds a venue .
  

</dd>
<dt class="callable" id="addVenueMapListener">
/sdk-for-flutter-navigate-venue-service-venueservice-addvenuemaplistener(<wbr/>/sdk-for-flutter-navigate-venue-service-venuemaplistener-class listener)
    → void

</dt>
<dd>
  Adds a venue map .
  

</dd>
<dt class="callable" id="addVenueToLoad">
/sdk-for-flutter-navigate-venue-service-venueservice-addvenuetoload(<wbr/>int venueId)
    → void

</dt>
<dd>
  Adds a venue to the loading queue.
  

</dd>
<dt class="callable" id="addVenueToLoadStr">
/sdk-for-flutter-navigate-venue-service-venueservice-addvenuetoloadstr(<wbr/>String venueIdentifier)
    → void

</dt>
<dd>
  Adds a venue to the loading queue.
  

</dd>
<dt class="callable" id="getInitStatus">
/sdk-for-flutter-navigate-venue-service-venueservice-getinitstatus(<wbr/>)
    → /sdk-for-flutter-navigate-venue-service-venueserviceinitstatus

</dt>
<dd>
  Gets an initialization status.
  

</dd>
<dt class="callable" id="isInitialized">
/sdk-for-flutter-navigate-venue-service-venueservice-isinitialized(<wbr/>)
    → bool

</dt>
<dd>
  Checks if the venue service is initialized.
  

</dd>
<dt class="callable" id="loadOptionalFeatures">
/sdk-for-flutter-navigate-venue-service-venueservice-loadoptionalfeatures(<wbr/>/sdk-for-flutter-navigate-venue-service-venueservicevenueoptionalfeaturelist optionalFeatureList)
    → void

</dt>
<dd>
  Lets user load optional features for current session.
  

</dd>
<dt class="callable" id="loadTopologies">
/sdk-for-flutter-navigate-venue-service-venueservice-loadtopologies(<wbr/>)
    → void

</dt>
<dd>
  Lets user load topologies for current session
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-venue-service-venueservice-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeServiceListener">
/sdk-for-flutter-navigate-venue-service-venueservice-removeservicelistener(<wbr/>/sdk-for-flutter-navigate-venue-service-venueservicelistener-class listener)
    → void

</dt>
<dd>
  Removes a service .
  

</dd>
<dt class="callable" id="removeVenueListener">
/sdk-for-flutter-navigate-venue-service-venueservice-removevenuelistener(<wbr/>/sdk-for-flutter-navigate-venue-service-venuelistener-class listener)
    → void

</dt>
<dd>
  Removes a venue .
  

</dd>
<dt class="callable" id="removeVenueMapListener">
/sdk-for-flutter-navigate-venue-service-venueservice-removevenuemaplistener(<wbr/>/sdk-for-flutter-navigate-venue-service-venuemaplistener-class listener)
    → void

</dt>
<dd>
  Removes a venue map .
  

</dd>
<dt class="callable" id="setHrn">
/sdk-for-flutter-navigate-venue-service-venueservice-sethrn(<wbr/>String hrn)
    → void

</dt>
<dd>
  Sets HRN of platform catalog.
  

</dd>
<dt class="callable" id="setLabeltextPreference">
/sdk-for-flutter-navigate-venue-service-venueservice-setlabeltextpreference(<wbr/>List&lt;<wbr/>String&gt; labelTextPref)
    → void

</dt>
<dd>
  Sets override labelTextPreference for labels.
  

</dd>
<dt class="callable" id="stop">
/sdk-for-flutter-navigate-venue-service-venueservice-stop(<wbr/>)
    → void

</dt>
<dd>
  Stops the venue service.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-service-venueservice-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-venue-service-venueservice-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li class="self-crumb">VenueService class</li>
</ol>
<h5>venue.service library</h5>
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
