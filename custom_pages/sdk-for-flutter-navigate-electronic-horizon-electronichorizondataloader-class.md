---
title: "ElectronicHorizonDataLoader class abstract"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonDataLoader-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="electronic_horizon/ElectronicHorizonDataLoader-class.html#constructors">Constructors</a></li>
<li><a href="electronic_horizon/ElectronicHorizonDataLoader/ElectronicHorizonDataLoader.html">ElectronicHorizonDataLoader</a></li>
<li class="section-title inherited">
<a href="electronic_horizon/ElectronicHorizonDataLoader-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonDataLoader/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonDataLoader/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="electronic_horizon/ElectronicHorizonDataLoader-class.html#instance-methods">Methods</a></li>
<li><a href="electronic_horizon/ElectronicHorizonDataLoader/addElectronicHorizonDataLoaderStatusListener.html">addElectronicHorizonDataLoaderStatusListener</a></li>
<li><a href="electronic_horizon/ElectronicHorizonDataLoader/getSegment.html">getSegment</a></li>
<li><a href="electronic_horizon/ElectronicHorizonDataLoader/loadData.html">loadData</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonDataLoader/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="electronic_horizon/ElectronicHorizonDataLoader/removeElectronicHorizonDataLoaderStatusListener.html">removeElectronicHorizonDataLoaderStatusListener</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonDataLoader/toString.html">toString</a></li>
<li class="section-title inherited"><a href="electronic_horizon/ElectronicHorizonDataLoader-class.html#operators">Operators</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonDataLoader/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li class="self-crumb">ElectronicHorizonDataLoader class</li>
</ol>
<div class="self-name">ElectronicHorizonDataLoader</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonDataLoader-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonDataLoader class abstract</h1></div>
<section class="desc markdown">
<p>Loads map data for segments that belong to the /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class paths.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ElectronicHorizonDataLoader">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-electronichorizondataloader(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class options, int segmentDataCacheSize)
</dt>
<dd>
          Creates a new instance of /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-runtimetype
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
<dt class="callable" id="addElectronicHorizonDataLoaderStatusListener">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-addelectronichorizondataloaderstatuslistener(<wbr/>/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderstatuslistener-class electronicHorizonListener)
    → void

</dt>
<dd>
  Adds an /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderstatuslistener-class to the subscription list.
  

</dd>
<dt class="callable" id="getSegment">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-getsegment(<wbr/>/sdk-for-flutter-navigate-mapdata-directedocmsegmentid-class segmentId)
    → /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderresult-class

</dt>
<dd>
  Returns loaded data for the given segment identifier.
  

</dd>
<dt class="callable" id="loadData">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-loaddata(<wbr/>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-class electronicHorizonUpdate)
    → void

</dt>
<dd>
  Requests data for all added segments and removes cached data for segments that are not part of the horizon anymore.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeElectronicHorizonDataLoaderStatusListener">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-removeelectronichorizondataloaderstatuslistener(<wbr/>/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderstatuslistener-class electronicHorizonListener)
    → void

</dt>
<dd>
  Removes an /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderstatuslistener-class from the subscription list.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">ElectronicHorizonDataLoader class</li>
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
