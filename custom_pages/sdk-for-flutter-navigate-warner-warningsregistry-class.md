---
title: "WarningsRegistry class abstract"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WarningsRegistry-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="warner/WarningsRegistry-class.html#constructors">Constructors</a></li>
<li><a href="warner/WarningsRegistry/WarningsRegistry.html">WarningsRegistry</a></li>
<li class="section-title inherited">
<a href="warner/WarningsRegistry-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="warner/WarningsRegistry/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="warner/WarningsRegistry/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="warner/WarningsRegistry-class.html#instance-methods">Methods</a></li>
<li><a href="warner/WarningsRegistry/getBorderCrossingWarning.html">getBorderCrossingWarning</a></li>
<li><a href="warner/WarningsRegistry/getCustomWarning.html">getCustomWarning</a></li>
<li><a href="warner/WarningsRegistry/getDangerZoneWarning.html">getDangerZoneWarning</a></li>
<li><a href="warner/WarningsRegistry/getEnvironmentalZoneWarning.html">getEnvironmentalZoneWarning</a></li>
<li><a href="warner/WarningsRegistry/getLaneDecreaseWarning.html">getLaneDecreaseWarning</a></li>
<li><a href="warner/WarningsRegistry/getLowSpeedZoneWarning.html">getLowSpeedZoneWarning</a></li>
<li><a href="warner/WarningsRegistry/getRailwayCrossingWarning.html">getRailwayCrossingWarning</a></li>
<li><a href="warner/WarningsRegistry/getRealisticViewWarning.html">getRealisticViewWarning</a></li>
<li><a href="warner/WarningsRegistry/getRoadSignWarning.html">getRoadSignWarning</a></li>
<li><a href="warner/WarningsRegistry/getSafetyCameraWarning.html">getSafetyCameraWarning</a></li>
<li><a href="warner/WarningsRegistry/getSchoolZoneWarning.html">getSchoolZoneWarning</a></li>
<li><a href="warner/WarningsRegistry/getTollStopWarning.html">getTollStopWarning</a></li>
<li><a href="warner/WarningsRegistry/getTrafficMergeWarning.html">getTrafficMergeWarning</a></li>
<li><a href="warner/WarningsRegistry/getTruckRestrictionWarning.html">getTruckRestrictionWarning</a></li>
<li class="inherited"><a href="warner/WarningsRegistry/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="warner/WarningsRegistry/toString.html">toString</a></li>
<li class="section-title inherited"><a href="warner/WarningsRegistry-class.html#operators">Operators</a></li>
<li class="inherited"><a href="warner/WarningsRegistry/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li class="self-crumb">WarningsRegistry class</li>
</ol>
<div class="self-name">WarningsRegistry</div>
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
<div class="main-content" data-above-sidebar="warner/warner-library-sidebar.html" data-below-sidebar="warner/WarningsRegistry-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>WarningsRegistry class abstract</h1></div>
<section class="desc markdown">
<p>A class that store warning metadata for different warning types.</p>
<p>Aggregates individual collection for each warning category (safety cameras, truck restrictions, etc.).
Provided by <code>WarnerEngine</code> so callers can lookup detailed information about specific warnings.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="WarningsRegistry">
/sdk-for-flutter-navigate-warner-warningsregistry-warningsregistry()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-warner-warningsregistry-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-warner-warningsregistry-runtimetype
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
<dt class="callable" id="getBorderCrossingWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-getbordercrossingwarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-bordercrossingwarning-class?

</dt>
<dd>
  Returns a border crossing warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getCustomWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-getcustomwarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-warner-customwarning-class?

</dt>
<dd>
  Returns additional data associated with the given custom warning.
  

</dd>
<dt class="callable" id="getDangerZoneWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-getdangerzonewarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-dangerzonewarning-class?

</dt>
<dd>
  Returns a danger zone warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getEnvironmentalZoneWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-getenvironmentalzonewarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-environmentalzonewarning-class?

</dt>
<dd>
  Returns environmental zone warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getLaneDecreaseWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-getlanedecreasewarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-warner-lanedecreasewarning-class?

</dt>
<dd>
  Returns a lane decrease warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getLowSpeedZoneWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-getlowspeedzonewarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-lowspeedzonewarning-class?

</dt>
<dd>
  Returns a low speed zone warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getRailwayCrossingWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-getrailwaycrossingwarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class?

</dt>
<dd>
  Returns a railway crossing warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getRealisticViewWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-getrealisticviewwarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-realisticviewwarning-class?

</dt>
<dd>
  Returns a realistic-view warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getRoadSignWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-getroadsignwarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-roadsignwarning-class?

</dt>
<dd>
  Returns a road-sign warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getSafetyCameraWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-getsafetycamerawarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-safetycamerawarning-class?

</dt>
<dd>
  Returns a safety-camera warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getSchoolZoneWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-getschoolzonewarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-schoolzonewarning-class?

</dt>
<dd>
  Returns a school zone warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getTollStopWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-gettollstopwarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-tollstop-class?

</dt>
<dd>
  Returns a toll stop warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getTrafficMergeWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-gettrafficmergewarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-trafficmergewarning-class?

</dt>
<dd>
  Returns a traffic merge warning corresponding to the given identifier.
  

</dd>
<dt class="callable" id="getTruckRestrictionWarning">
/sdk-for-flutter-navigate-warner-warningsregistry-gettruckrestrictionwarning(<wbr/>/sdk-for-flutter-navigate-warner-warning-class warning)
    → /sdk-for-flutter-navigate-navigation-truckrestrictionwarning-class?

</dt>
<dd>
  Returns a truck restrictions warning corresponding to the given identifier.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-warner-warningsregistry-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-warner-warningsregistry-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-warner-warningsregistry-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li class="self-crumb">WarningsRegistry class</li>
</ol>
<h5>warner library</h5>
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
