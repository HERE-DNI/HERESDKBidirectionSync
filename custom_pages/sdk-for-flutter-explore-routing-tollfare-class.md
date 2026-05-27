---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-tollfare-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TollFare-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/TollFare-class.html#constructors">Constructors</a></li>
<li><a href="routing/TollFare/TollFare.html">TollFare</a></li>
<li class="section-title">
<a href="routing/TollFare-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/TollFare/currency.html">currency</a></li>
<li><a href="routing/TollFare/hashCode.html">hashCode</a></li>
<li><a href="routing/TollFare/pass.html">pass</a></li>
<li><a href="routing/TollFare/paymentMethods.html">paymentMethods</a></li>
<li><a href="routing/TollFare/price.html">price</a></li>
<li class="inherited"><a href="routing/TollFare/runtimeType.html">runtimeType</a></li>
<li><a href="routing/TollFare/timeRule.html">timeRule</a></li>
<li><a href="routing/TollFare/transponders.html">transponders</a></li>
<li class="section-title inherited"><a href="routing/TollFare-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/TollFare/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/TollFare/toString.html">toString</a></li>
<li class="section-title"><a href="routing/TollFare-class.html#operators">Operators</a></li>
<li><a href="routing/TollFare/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
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
<a href="../routing/TollFare/TollFare.html">/sdk-for-flutter-explore-routing-tollfare-tollfare</a>(String currency, double price, List&lt;<wbr/><a href="../routing/PaymentMethod.html">/sdk-for-flutter-explore-routing-paymentmethod</a>&gt; paymentMethods, [<a href="../core/TimeRule-class.html">/sdk-for-flutter-explore-core-timerule-class</a>? timeRule = null, List&lt;<wbr/>String&gt; transponders = const [], <a href="../routing/TollFarePass-class.html">/sdk-for-flutter-explore-routing-tollfarepass-class</a>? pass = null])
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
<a href="../routing/TollFare/currency.html">/sdk-for-flutter-explore-routing-tollfare-currency</a>
↔ String
</dt>
<dd>
  The currency in which the toll is to be paid in ISO 4217 format, e.g. "USD".
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/TollFare/hashCode.html">/sdk-for-flutter-explore-routing-tollfare-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="pass">
<a href="../routing/TollFare/pass.html">/sdk-for-flutter-explore-routing-tollfare-pass</a>
↔ <a href="../routing/TollFarePass-class.html">/sdk-for-flutter-explore-routing-tollfarepass-class</a>?
</dt>
<dd>
  Specifies whether this <a href="../routing/TollFare-class.html">/sdk-for-flutter-explore-routing-tollfare-class</a> is a multi-travel pass, and its characteristics.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="paymentMethods">
<a href="../routing/TollFare/paymentMethods.html">/sdk-for-flutter-explore-routing-tollfare-paymentmethods</a>
↔ List&lt;<wbr/><a href="../routing/PaymentMethod.html">/sdk-for-flutter-explore-routing-paymentmethod</a>&gt;
</dt>
<dd>
  The list of accepted payment methods like cash and credit card.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="price">
<a href="../routing/TollFare/price.html">/sdk-for-flutter-explore-routing-tollfare-price</a>
↔ double
</dt>
<dd>
  The amount of the toll be paid.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/TollFare/runtimeType.html">/sdk-for-flutter-explore-routing-tollfare-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="timeRule">
<a href="../routing/TollFare/timeRule.html">/sdk-for-flutter-explore-routing-tollfare-timerule</a>
↔ <a href="../core/TimeRule-class.html">/sdk-for-flutter-explore-core-timerule-class</a>?
</dt>
<dd>
  The time domain when this fare is valid.
If this field is missing, it means the fare is always valid.
For a detailed description of the Time Domain specification and usage in routing services, please refer to
the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a>
<div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="transponders">
<a href="../routing/TollFare/transponders.html">/sdk-for-flutter-explore-routing-tollfare-transponders</a>
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
<a href="../routing/TollFare/noSuchMethod.html">/sdk-for-flutter-explore-routing-tollfare-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/TollFare/toString.html">/sdk-for-flutter-explore-routing-tollfare-tostring</a>(<wbr/>)
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
<a href="../routing/TollFare/operator_equals.html">/sdk-for-flutter-explore-routing-tollfare-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
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
</div></div>
</div>
</HTMLBlock>
