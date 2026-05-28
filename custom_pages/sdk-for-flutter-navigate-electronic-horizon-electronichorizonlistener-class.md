---
title: "ElectronicHorizonListener class abstract"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonListener-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="electronic_horizon/ElectronicHorizonListener-class.html#constructors">Constructors</a></li>
<li><a href="electronic_horizon/ElectronicHorizonListener/ElectronicHorizonListener.html">ElectronicHorizonListener</a></li>
<li class="section-title inherited">
<a href="electronic_horizon/ElectronicHorizonListener-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonListener/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonListener/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="electronic_horizon/ElectronicHorizonListener-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonListener/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="electronic_horizon/ElectronicHorizonListener/onElectronicHorizonUpdated.html">onElectronicHorizonUpdated</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonListener/toString.html">toString</a></li>
<li class="section-title inherited"><a href="electronic_horizon/ElectronicHorizonListener-class.html#operators">Operators</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonListener/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li class="self-crumb">ElectronicHorizonListener class</li>
</ol>
<div class="self-name">ElectronicHorizonListener</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonListener class abstract</h1></div>
<section class="desc markdown">
<p>Provides a listener for receiving updates during execution of the /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-update method.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implementers</dt>
<dd><ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-warner-warnerengine-class</li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ElectronicHorizonListener">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-electronichorizonlistener(void onElectronicHorizonUpdatedLambda(/sdk-for-flutter-navigate-electronic-horizon-electronichorizonerrorcode?, /sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-class?))
</dt>
<dd>
          Provides a listener for receiving updates during execution of the /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-update method.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-runtimetype
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
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onElectronicHorizonUpdated">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-onelectronichorizonupdated(<wbr/>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonerrorcode? errorCode, /sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-class? update)
    → void

</dt>
<dd>
  Called whenever the electronic horizon subsystem produces:
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li class="self-crumb">ElectronicHorizonListener class</li>
</ol>
<h5>electronic_horizon library</h5>
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
