---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-evseinfo-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVSEInfo-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">EVSEInfo class</li>
</ol>
<div class="self-name">EVSEInfo</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVSEInfo-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVSEInfo class</h1></div>
<section class="desc markdown">
<p>Represents an EVSE at the charging point.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVSEInfo">
/sdk-for-flutter-navigate-search-evseinfo-evseinfo()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="capabilities">
/sdk-for-flutter-navigate-search-evseinfo-capabilities
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-ev-evsecapability&gt;
</dt>
<dd>
  Capabilities of the EVSE.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectors">
/sdk-for-flutter-navigate-search-evseinfo-connectors
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-search-evchargingconnector-class&gt;
</dt>
<dd>
  List of available connectors on the EVSE. An operational EVSE should have at least one connector.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="coordinates">
/sdk-for-flutter-navigate-search-evseinfo-coordinates
↔ /sdk-for-flutter-navigate-core-geocoordinates-class?
</dt>
<dd>
  The geographic coordinates of the EVSE.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="evseID">
/sdk-for-flutter-navigate-search-evseinfo-evseid
↔ String?
</dt>
<dd>
  Identifier compliant with the EVSE ID from eMI3 standard version V1.0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="floorLevel">
/sdk-for-flutter-navigate-search-evseinfo-floorlevel
↔ String?
</dt>
<dd>
  Floor level on which the EVSE is located.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-search-evseinfo-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-search-evseinfo-id
↔ String?
</dt>
<dd>
  Human-readable globally unique identifier for the EVSE.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lastUpdated">
/sdk-for-flutter-navigate-search-evseinfo-lastupdated
↔ DateTime
</dt>
<dd>
  Timestamp when the status of this EVSE was last updated.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="paymentSupports">
/sdk-for-flutter-navigate-search-evseinfo-paymentsupports
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-ev-evsepaymentsupport&gt;
</dt>
<dd>
  List of payment support functionalities on EVSE for ad-hoc customers (without pre-registration).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="physicalReference">
/sdk-for-flutter-navigate-search-evseinfo-physicalreference
↔ String?
</dt>
<dd>
  A number or string printed on the outside of the EVSE for visual identification.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-search-evseinfo-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="status">
/sdk-for-flutter-navigate-search-evseinfo-status
↔ /sdk-for-flutter-navigate-ev-evsestate
</dt>
<dd>
  Status of the EVSE.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="uid">
/sdk-for-flutter-navigate-search-evseinfo-uid
↔ String
</dt>
<dd>
  Uniquely identifies the EVSE within the CPOs platform (and suboperator platforms).
For example a database ID or the actual "EVSE ID". This field can never be changed, modified or renamed.
This is the 'technical' identification of the EVSE, not to be used as 'human readable' identification, use the field /sdk-for-flutter-navigate-search-evseinfo-id for that.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-search-evseinfo-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-search-evseinfo-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-search-evseinfo-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">EVSEInfo class</li>
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



</div>
`
}</HTMLBlock>
