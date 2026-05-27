---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-placefilterev-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- PlaceFilterEv-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/PlaceFilterEv-class.html#constructors">Constructors</a></li>
<li><a href="search/PlaceFilterEv/PlaceFilterEv.html">PlaceFilterEv</a></li>
<li class="section-title">
<a href="search/PlaceFilterEv-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/PlaceFilterEv/connectorTypeIDs.html">connectorTypeIDs</a></li>
<li><a href="search/PlaceFilterEv/currentType.html">currentType</a></li>
<li><a href="search/PlaceFilterEv/eMobilityServiceProviderPartnerIDs.html">eMobilityServiceProviderPartnerIDs</a></li>
<li><a href="search/PlaceFilterEv/hashCode.html">hashCode</a></li>
<li><a href="search/PlaceFilterEv/minPowerInKilowatts.html">minPowerInKilowatts</a></li>
<li class="inherited"><a href="search/PlaceFilterEv/runtimeType.html">runtimeType</a></li>
<li><a href="search/PlaceFilterEv/supplierNames.html">supplierNames</a></li>
<li class="section-title inherited"><a href="search/PlaceFilterEv-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/PlaceFilterEv/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/PlaceFilterEv/toString.html">toString</a></li>
<li class="section-title"><a href="search/PlaceFilterEv-class.html#operators">Operators</a></li>
<li><a href="search/PlaceFilterEv/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">PlaceFilterEv class</li>
</ol>
<div class="self-name">PlaceFilterEv</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/PlaceFilterEv-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PlaceFilterEv class</h1></div>
<section class="desc markdown">
<p>Constraints that are applicable on the places of category EV station.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PlaceFilterEv">
<a href="../search/PlaceFilterEv/PlaceFilterEv.html">/sdk-for-flutter-explore-search-placefilterev-placefilterev</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="connectorTypeIDs">
<a href="../search/PlaceFilterEv/connectorTypeIDs.html">/sdk-for-flutter-explore-search-placefilterev-connectortypeids</a>
↔ List&lt;<wbr/>String&gt;
</dt>
<dd>
  Filter to retrieve EV charging stations with at least one of the connector type IDs.
For more information on the current connector types, see
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-type-connector.html</a>
<div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="currentType">
<a href="../search/PlaceFilterEv/currentType.html">/sdk-for-flutter-explore-search-placefilterev-currenttype</a>
↔ <a href="../core/CurrentType.html">/sdk-for-flutter-explore-core-currenttype</a>?
</dt>
<dd>
  Filter to retrieve EV charging stations with the given current type
provided at one of the station EVSE. Accepted is either AC or DC.
Not supported for <code>suggestByText</code> in <code>OfflineSearchEngine</code> (only available for the Navigate license).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="eMobilityServiceProviderPartnerIDs">
<a href="../search/PlaceFilterEv/eMobilityServiceProviderPartnerIDs.html">/sdk-for-flutter-explore-search-placefilterev-emobilityserviceproviderpartnerids</a>
↔ List&lt;<wbr/>String&gt;
</dt>
<dd>
  Filter to retrieve EV charging stations with at least one matching e-Mobility Service Provider Partner ID.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/PlaceFilterEv/hashCode.html">/sdk-for-flutter-explore-search-placefilterev-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="minPowerInKilowatts">
<a href="../search/PlaceFilterEv/minPowerInKilowatts.html">/sdk-for-flutter-explore-search-placefilterev-minpowerinkilowatts</a>
↔ double?
</dt>
<dd>
  Filter to retrieve EV charging stations with the given minimum charging power in KW
delivered by at least one of the station EVSE.
Not supported for <code>suggestByText</code> in <code>OfflineSearchEngine</code> (only available for the Navigate license).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/PlaceFilterEv/runtimeType.html">/sdk-for-flutter-explore-search-placefilterev-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="supplierNames">
<a href="../search/PlaceFilterEv/supplierNames.html">/sdk-for-flutter-explore-search-placefilterev-suppliernames</a>
↔ List&lt;<wbr/>String&gt;
</dt>
<dd>
  Sets a constraint on the charge point operator name of the EV station.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/PlaceFilterEv/noSuchMethod.html">/sdk-for-flutter-explore-search-placefilterev-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/PlaceFilterEv/toString.html">/sdk-for-flutter-explore-search-placefilterev-tostring</a>(<wbr/>)
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
<a href="../search/PlaceFilterEv/operator_equals.html">/sdk-for-flutter-explore-search-placefilterev-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">PlaceFilterEv class</li>
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
</div></div>
</div>
</HTMLBlock>
