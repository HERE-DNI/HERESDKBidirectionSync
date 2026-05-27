---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-routingconnectionsettings-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RoutingConnectionSettings-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/RoutingConnectionSettings-class.html#constructors">Constructors</a></li>
<li><a href="routing/RoutingConnectionSettings/RoutingConnectionSettings.html">RoutingConnectionSettings</a></li>
<li class="section-title">
<a href="routing/RoutingConnectionSettings-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/RoutingConnectionSettings/connectionTimeoutRetryIncrease.html">connectionTimeoutRetryIncrease</a></li>
<li><a href="routing/RoutingConnectionSettings/hashCode.html">hashCode</a></li>
<li><a href="routing/RoutingConnectionSettings/initialConnectionTimeout.html">initialConnectionTimeout</a></li>
<li><a href="routing/RoutingConnectionSettings/initialTransferTimeout.html">initialTransferTimeout</a></li>
<li><a href="routing/RoutingConnectionSettings/maxRetryCount.html">maxRetryCount</a></li>
<li class="inherited"><a href="routing/RoutingConnectionSettings/runtimeType.html">runtimeType</a></li>
<li><a href="routing/RoutingConnectionSettings/transferTimeoutRetryIncrease.html">transferTimeoutRetryIncrease</a></li>
<li class="section-title inherited"><a href="routing/RoutingConnectionSettings-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/RoutingConnectionSettings/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/RoutingConnectionSettings/toString.html">toString</a></li>
<li class="section-title"><a href="routing/RoutingConnectionSettings-class.html#operators">Operators</a></li>
<li><a href="routing/RoutingConnectionSettings/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">RoutingConnectionSettings class</li>
</ol>
<div class="self-name">RoutingConnectionSettings</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RoutingConnectionSettings-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RoutingConnectionSettings class</h1></div>
<section class="desc markdown">
<p>Defines the settings for the retry logic when connecting to the HERE routing backend.</p>
<p>When a timeout is triggered,
the next connection attempt starts with a increased timeout.
new_timeout = initial_timeout + increment * retry_count</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RoutingConnectionSettings">
<a href="../routing/RoutingConnectionSettings/RoutingConnectionSettings.html">/sdk-for-flutter-explore-routing-routingconnectionsettings-routingconnectionsettings</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="connectionTimeoutRetryIncrease">
<a href="../routing/RoutingConnectionSettings/connectionTimeoutRetryIncrease.html">/sdk-for-flutter-explore-routing-routingconnectionsettings-connectiontimeoutretryincrease</a>
↔ Duration
</dt>
<dd>
  Defines the increase of the timeout for the transfer of data.
By default, the initial connection increment per timeout 10 seconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/RoutingConnectionSettings/hashCode.html">/sdk-for-flutter-explore-routing-routingconnectionsettings-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="initialConnectionTimeout">
<a href="../routing/RoutingConnectionSettings/initialConnectionTimeout.html">/sdk-for-flutter-explore-routing-routingconnectionsettings-initialconnectiontimeout</a>
↔ Duration
</dt>
<dd>
  Defines the initial time out for connection to the backend.
By default, the initial connection timeout is 5 seconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="initialTransferTimeout">
<a href="../routing/RoutingConnectionSettings/initialTransferTimeout.html">/sdk-for-flutter-explore-routing-routingconnectionsettings-initialtransfertimeout</a>
↔ Duration
</dt>
<dd>
  Defines the initial time out for data transfer from the backend.
By default, the initial transfer timeout is 10 seconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxRetryCount">
<a href="../routing/RoutingConnectionSettings/maxRetryCount.html">/sdk-for-flutter-explore-routing-routingconnectionsettings-maxretrycount</a>
↔ int
</dt>
<dd>
  Defines the max amount of retries before the route request failes with connection related error codes.
By default, the max amount of retries is 3.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/RoutingConnectionSettings/runtimeType.html">/sdk-for-flutter-explore-routing-routingconnectionsettings-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="transferTimeoutRetryIncrease">
<a href="../routing/RoutingConnectionSettings/transferTimeoutRetryIncrease.html">/sdk-for-flutter-explore-routing-routingconnectionsettings-transfertimeoutretryincrease</a>
↔ Duration
</dt>
<dd>
  Defines the increase of the timeout for the connection.
By default, the initial transfer increment per timeout is 2 seconds.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/RoutingConnectionSettings/noSuchMethod.html">/sdk-for-flutter-explore-routing-routingconnectionsettings-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/RoutingConnectionSettings/toString.html">/sdk-for-flutter-explore-routing-routingconnectionsettings-tostring</a>(<wbr/>)
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
<a href="../routing/RoutingConnectionSettings/operator_equals.html">/sdk-for-flutter-explore-routing-routingconnectionsettings-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">RoutingConnectionSettings class</li>
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
