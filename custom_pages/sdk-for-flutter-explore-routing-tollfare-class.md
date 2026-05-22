---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-tollfare-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollFare-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">TollFare class</li>
</ol>
<div class="self-name">TollFare</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TollFare-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TollFare class</h1></div>
<section class="desc markdown">
<p>This struct presents all the fare data for a toll.</p>
<p><strong>Note</strong>: If you're using the <code>OfflineRoutingEngine</code>, be aware that this feature is
currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
Additionally, this feature and related APIs may be updated in future releases
without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
is only available for the Navigate license. If you're using the
<code>RoutingEngine</code>, this feature is considered to be stable.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TollFare">
/sdk-for-flutter-explore-routing-tollfare-tollfare(String currency, double price, List&lt;<wbr/>/sdk-for-flutter-explore-routing-paymentmethod&gt; paymentMethods, [/sdk-for-flutter-explore-core-timerule-class? timeRule = null, List&lt;<wbr/>String&gt; transponders = const [], /sdk-for-flutter-explore-routing-tollfarepass-class? pass = null])
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="currency">
/sdk-for-flutter-explore-routing-tollfare-currency
↔ String
</dt>
<dd>
  The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-routing-tollfare-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="pass">
/sdk-for-flutter-explore-routing-tollfare-pass
↔ /sdk-for-flutter-explore-routing-tollfarepass-class?
</dt>
<dd>
  Specifies whether this /sdk-for-flutter-explore-routing-tollfare-class is a multi-travel pass, and its characteristics.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="paymentMethods">
/sdk-for-flutter-explore-routing-tollfare-paymentmethods
↔ List&lt;<wbr/>/sdk-for-flutter-explore-routing-paymentmethod&gt;
</dt>
<dd>
  The list of accepted payment methods like cash and credit card.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="price">
/sdk-for-flutter-explore-routing-tollfare-price
↔ double
</dt>
<dd>
  The amount of the toll be paid.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-tollfare-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="timeRule">
/sdk-for-flutter-explore-routing-tollfare-timerule
↔ /sdk-for-flutter-explore-core-timerule-class?
</dt>
<dd>
  The time domain when this fare is valid.
If this field is missing, it means the fare is always valid.
For a detailed description of the Time Domain specification and usage in routing services, please refer to
the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a>
<div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="transponders">
/sdk-for-flutter-explore-routing-tollfare-transponders
↔ List&lt;<wbr/>String&gt;
</dt>
<dd>
  The list of available transponders.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-routing-tollfare-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-tollfare-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-tollfare-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">TollFare class</li>
</ol>
<h5>routing library</h5>
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
