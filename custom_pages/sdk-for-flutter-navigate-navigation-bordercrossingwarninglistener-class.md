---
title: "BorderCrossingWarningListener class abstract"
slug: "sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- BorderCrossingWarningListener-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/BorderCrossingWarningListener-class.html#constructors">Constructors</a></li>
<li><a href="navigation/BorderCrossingWarningListener/BorderCrossingWarningListener.html">BorderCrossingWarningListener</a></li>
<li class="section-title inherited">
<a href="navigation/BorderCrossingWarningListener-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="navigation/BorderCrossingWarningListener/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="navigation/BorderCrossingWarningListener/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="navigation/BorderCrossingWarningListener-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/BorderCrossingWarningListener/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="navigation/BorderCrossingWarningListener/onBorderCrossingWarningUpdated.html">onBorderCrossingWarningUpdated</a></li>
<li class="inherited"><a href="navigation/BorderCrossingWarningListener/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/BorderCrossingWarningListener-class.html#operators">Operators</a></li>
<li class="inherited"><a href="navigation/BorderCrossingWarningListener/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">BorderCrossingWarningListener class</li>
</ol>
<div class="self-name">BorderCrossingWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/BorderCrossingWarningListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>BorderCrossingWarningListener class abstract</h1></div>
<section class="desc markdown">
<p>This abstract class
should be implemented in order to receive border crossing warnings for country and state borders.</p>
<p><strong>Note:</strong> The border crossing warner is a point warner, which means that for a border crossing there will <em>always</em> be
2 warnings emitted, with the /sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetype set to /sdk-for-flutter-navigate-navigation-distancetype and /sdk-for-flutter-navigate-navigation-distancetype
which is given when the location of the border crossing is reached.
A /sdk-for-flutter-navigate-navigation-bordercrossingwarning-class will not be given until the previous warning of that type has been passed.
For example, a route with /sdk-for-flutter-navigate-navigation-bordercrossingwarning-class 120 meters and /sdk-for-flutter-navigate-navigation-bordercrossingwarning-class 160 meters ahead,
the first /sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetobordercrossinginmeters is 120 meters
and the next /sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetobordercrossinginmeters is then 40 meters,
since that is the distance between the first and second warnings.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="BorderCrossingWarningListener">
/sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-bordercrossingwarninglistener(void onBorderCrossingWarningUpdatedLambda(/sdk-for-flutter-navigate-navigation-bordercrossingwarning-class))
</dt>
<dd>
          This abstract class
should be implemented in order to receive border crossing warnings for country and state borders.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-runtimetype
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
/sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onBorderCrossingWarningUpdated">
/sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-onbordercrossingwarningupdated(<wbr/>/sdk-for-flutter-navigate-navigation-bordercrossingwarning-class borderCrossingWarning)
    → void

</dt>
<dd>
  Called whenever a new border crossing warning is available.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">BorderCrossingWarningListener class</li>
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
</div></div>
</div>
`
}</HTMLBlock>
