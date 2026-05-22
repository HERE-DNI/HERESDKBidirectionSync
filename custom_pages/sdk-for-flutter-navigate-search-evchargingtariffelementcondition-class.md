---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-evchargingtariffelementcondition-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingTariffElementCondition-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">EVChargingTariffElementCondition class</li>
</ol>
<div class="self-name">EVChargingTariffElementCondition</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingTariffElementCondition-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVChargingTariffElementCondition class</h1></div>
<section class="desc markdown">
<p>Condition that the charging session needs to meet to apply the tariff element.</p>
<p>Tariff elements may include conditions that define when they apply:</p>
<ul>
<li>Time of day (e.g., 22:00–06:00)</li>
<li>Day of week (e.g., weekends only)</li>
<li>Date range (e.g., seasonal pricing)</li>
<li>Charging session duration</li>
<li>Battery level thresholds (e.g., overstay fees)</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVChargingTariffElementCondition">
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-evchargingtariffelementcondition()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="date">
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-date
↔ /sdk-for-flutter-navigate-search-daterange-class?
</dt>
<dd>
  Date range when the tariff element is valid. This is typically used to indicate seasonal
tariffs or to announce an update to the tariff in advance. It may also be used to indicate
spot prices, together with time period.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="days">
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-days
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-search-dayofweek&gt;
</dt>
<dd>
  Day(s) of the week when the tariff element is valid.
An example would be to specify lower prices for weekends
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="duration">
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-duration
↔ /sdk-for-flutter-navigate-search-evchargingdurationrange-class?
</dt>
<dd>
  Duration of the charging session when the tariff element is valid, in seconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="overstayBatteryLevel">
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-overstaybatterylevel
↔ int?
</dt>
<dd>
  Minimum battery level when the tariff element is valid, in percentages. This can be used to
set additional fees for charging a full or nearly full battery.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="time">
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-time
↔ /sdk-for-flutter-navigate-search-timeofdayrange-class?
</dt>
<dd>
  Time period when the tariff element is valid, in local time. The time period wraps around to
the next day, when end time of the period /sdk-for-flutter-navigate-search-timeofdayrange-to
is smaller than the beginning /sdk-for-flutter-navigate-search-timeofdayrange-from.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-search-evchargingtariffelementcondition-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">EVChargingTariffElementCondition class</li>
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
