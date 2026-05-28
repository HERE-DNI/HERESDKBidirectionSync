---
title: "Metadata class abstract"
slug: "sdk-for-flutter-navigate-core-metadata-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Metadata-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/Metadata-class.html#constructors">Constructors</a></li>
<li><a href="core/Metadata/Metadata.html">Metadata</a></li>
<li class="section-title inherited">
<a href="core/Metadata-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="core/Metadata/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="core/Metadata/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="core/Metadata-class.html#instance-methods">Methods</a></li>
<li><a href="core/Metadata/getCustomValue.html">getCustomValue</a></li>
<li><a href="core/Metadata/getDouble.html">getDouble</a></li>
<li><a href="core/Metadata/getGeoCoordinates.html">getGeoCoordinates</a></li>
<li><a href="core/Metadata/getInteger.html">getInteger</a></li>
<li><a href="core/Metadata/getString.html">getString</a></li>
<li><a href="core/Metadata/getType.html">getType</a></li>
<li class="inherited"><a href="core/Metadata/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="core/Metadata/removeValue.html">removeValue</a></li>
<li><a href="core/Metadata/setCustomValue.html">setCustomValue</a></li>
<li><a href="core/Metadata/setDouble.html">setDouble</a></li>
<li><a href="core/Metadata/setGeoCoordinates.html">setGeoCoordinates</a></li>
<li><a href="core/Metadata/setInteger.html">setInteger</a></li>
<li><a href="core/Metadata/setString.html">setString</a></li>
<li class="inherited"><a href="core/Metadata/toString.html">toString</a></li>
<li class="section-title inherited"><a href="core/Metadata-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core/Metadata/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li class="self-crumb">Metadata class</li>
</ol>
<div class="self-name">Metadata</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/Metadata-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Metadata class abstract</h1></div>
<section class="desc markdown">
<p>Holds metadata on behalf of a map item.</p>
<p>An instance of this class can contain metadata items of varying types, such as
String, Integer, Double, GeoCoordinates etc. and can also hold arbitrary metadata
types by the use of the CustomMetadataValue abstract class.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Metadata">
/sdk-for-flutter-navigate-core-metadata-metadata()
</dt>
<dd>
          Creates an instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-core-metadata-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-metadata-runtimetype
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
<dt class="callable" id="getCustomValue">
/sdk-for-flutter-navigate-core-metadata-getcustomvalue(<wbr/>String key)
    → /sdk-for-flutter-navigate-core-custommetadatavalue-class?

</dt>
<dd>
  Obtains an instance of the CustomMetadataValue class associated with a given key.
  

</dd>
<dt class="callable" id="getDouble">
/sdk-for-flutter-navigate-core-metadata-getdouble(<wbr/>String key)
    → double?

</dt>
<dd>
  Obtains a Double value associated with a given key.
  

</dd>
<dt class="callable" id="getGeoCoordinates">
/sdk-for-flutter-navigate-core-metadata-getgeocoordinates(<wbr/>String key)
    → /sdk-for-flutter-navigate-core-geocoordinates-class?

</dt>
<dd>
  Obtains a GeoCoordinates value associated with a given key.
  

</dd>
<dt class="callable" id="getInteger">
/sdk-for-flutter-navigate-core-metadata-getinteger(<wbr/>String key)
    → int?

</dt>
<dd>
  Obtains an Integer value associated with a given key.
  

</dd>
<dt class="callable" id="getString">
/sdk-for-flutter-navigate-core-metadata-getstring(<wbr/>String key)
    → String?

</dt>
<dd>
  Obtains a String value associated with a given key.
  

</dd>
<dt class="callable" id="getType">
/sdk-for-flutter-navigate-core-metadata-gettype(<wbr/>String key)
    → /sdk-for-flutter-navigate-core-metadatatype?

</dt>
<dd>
  Determines the type of a metadata value.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-core-metadata-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeValue">
/sdk-for-flutter-navigate-core-metadata-removevalue(<wbr/>String key)
    → void

</dt>
<dd>
  Removes a metadata key and its associated value.
  

</dd>
<dt class="callable" id="setCustomValue">
/sdk-for-flutter-navigate-core-metadata-setcustomvalue(<wbr/>String key, /sdk-for-flutter-navigate-core-custommetadatavalue-class value)
    → void

</dt>
<dd>
  Creates a key:value pair, where the value is a type derived from CustomMetadataValue.
  

</dd>
<dt class="callable" id="setDouble">
/sdk-for-flutter-navigate-core-metadata-setdouble(<wbr/>String key, double value)
    → void

</dt>
<dd>
  Creates a key:value pair, where the value is of type Double.
  

</dd>
<dt class="callable" id="setGeoCoordinates">
/sdk-for-flutter-navigate-core-metadata-setgeocoordinates(<wbr/>String key, /sdk-for-flutter-navigate-core-geocoordinates-class value)
    → void

</dt>
<dd>
  Creates a key:value pair, where the value is of type GeoCoordinates.
  

</dd>
<dt class="callable" id="setInteger">
/sdk-for-flutter-navigate-core-metadata-setinteger(<wbr/>String key, int value)
    → void

</dt>
<dd>
  Creates a key:value pair, where the value is of type Integer.
  

</dd>
<dt class="callable" id="setString">
/sdk-for-flutter-navigate-core-metadata-setstring(<wbr/>String key, String value)
    → void

</dt>
<dd>
  Creates a key:value pair, where the value is of type String.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-metadata-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-core-metadata-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li class="self-crumb">Metadata class</li>
</ol>
<h5>core library</h5>
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
