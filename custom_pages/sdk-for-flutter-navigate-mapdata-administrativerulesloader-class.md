---
title: "AdministrativeRulesLoader class abstract"
slug: "sdk-for-flutter-navigate-mapdata-administrativerulesloader-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AdministrativeRulesLoader-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapdata/AdministrativeRulesLoader-class.html#constructors">Constructors</a></li>
<li><a href="mapdata/AdministrativeRulesLoader/AdministrativeRulesLoader.html">AdministrativeRulesLoader</a></li>
<li><a href="mapdata/AdministrativeRulesLoader/AdministrativeRulesLoader.withEngine.html">withEngine</a></li>
<li class="section-title inherited">
<a href="mapdata/AdministrativeRulesLoader-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapdata/AdministrativeRulesLoader/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapdata/AdministrativeRulesLoader/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapdata/AdministrativeRulesLoader-class.html#instance-methods">Methods</a></li>
<li><a href="mapdata/AdministrativeRulesLoader/getAdministrativeRules.html">getAdministrativeRules</a></li>
<li><a href="mapdata/AdministrativeRulesLoader/getStateCodes.html">getStateCodes</a></li>
<li class="inherited"><a href="mapdata/AdministrativeRulesLoader/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapdata/AdministrativeRulesLoader/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapdata/AdministrativeRulesLoader-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapdata/AdministrativeRulesLoader/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">AdministrativeRulesLoader class</li>
</ol>
<div class="self-name">AdministrativeRulesLoader</div>
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
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/AdministrativeRulesLoader-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>AdministrativeRulesLoader class abstract</h1></div>
<section class="desc markdown">
<p>Provides the abstract class for the access to the administrative rules available
for a country or a state in the local OCM map.</p>
<p>Please be aware that the methods within this
classload map data synchronously. In the event of absent data in the disk cache, the data
will be retrieved from the remote server. To mitigate the potential freezing of the calling
thread, it is advisable to proactively prefetch map data around the working area.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="AdministrativeRulesLoader">
/sdk-for-flutter-navigate-mapdata-administrativerulesloader-administrativerulesloader()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="AdministrativeRulesLoader.withEngine">
/sdk-for-flutter-navigate-mapdata-administrativerulesloader-administrativerulesloader-withengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapdata-administrativerulesloader-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-administrativerulesloader-runtimetype
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
<dt class="callable" id="getAdministrativeRules">
/sdk-for-flutter-navigate-mapdata-administrativerulesloader-getadministrativerules(<wbr/>/sdk-for-flutter-navigate-core-countrycode countryCode, String? stateCode)
    → /sdk-for-flutter-navigate-mapdata-administrativerules-class

</dt>
<dd>
  Synchronously load the administrative rules for the specified country and state.
  

</dd>
<dt class="callable" id="getStateCodes">
/sdk-for-flutter-navigate-mapdata-administrativerulesloader-getstatecodes(<wbr/>/sdk-for-flutter-navigate-core-countrycode countryCode)
    → List&lt;<wbr/>String&gt;

</dt>
<dd>
  Synchronously loads the list of state codes from a specified country for which
administrative rules are availabe.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapdata-administrativerulesloader-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-administrativerulesloader-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapdata-administrativerulesloader-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">AdministrativeRulesLoader class</li>
</ol>
<h5>mapdata library</h5>
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
