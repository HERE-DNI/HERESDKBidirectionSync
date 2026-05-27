---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-metadata-class"
---

<HTMLBlock>
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
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
<a href="../core/Metadata/Metadata.html">/sdk-for-flutter-explore-core-metadata-metadata</a>()
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
<a href="../core/Metadata/hashCode.html">/sdk-for-flutter-explore-core-metadata-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core/Metadata/runtimeType.html">/sdk-for-flutter-explore-core-metadata-runtimetype</a>
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
<a href="../core/Metadata/getCustomValue.html">/sdk-for-flutter-explore-core-metadata-getcustomvalue</a>(<wbr/>String key)
    → <a href="../core/CustomMetadataValue-class.html">/sdk-for-flutter-explore-core-custommetadatavalue-class</a>?

</dt>
<dd>
  Obtains an instance of the CustomMetadataValue class associated with a given key.
  

</dd>
<dt class="callable" id="getDouble">
<a href="../core/Metadata/getDouble.html">/sdk-for-flutter-explore-core-metadata-getdouble</a>(<wbr/>String key)
    → double?

</dt>
<dd>
  Obtains a Double value associated with a given key.
  

</dd>
<dt class="callable" id="getGeoCoordinates">
<a href="../core/Metadata/getGeoCoordinates.html">/sdk-for-flutter-explore-core-metadata-getgeocoordinates</a>(<wbr/>String key)
    → <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>?

</dt>
<dd>
  Obtains a GeoCoordinates value associated with a given key.
  

</dd>
<dt class="callable" id="getInteger">
<a href="../core/Metadata/getInteger.html">/sdk-for-flutter-explore-core-metadata-getinteger</a>(<wbr/>String key)
    → int?

</dt>
<dd>
  Obtains an Integer value associated with a given key.
  

</dd>
<dt class="callable" id="getString">
<a href="../core/Metadata/getString.html">/sdk-for-flutter-explore-core-metadata-getstring</a>(<wbr/>String key)
    → String?

</dt>
<dd>
  Obtains a String value associated with a given key.
  

</dd>
<dt class="callable" id="getType">
<a href="../core/Metadata/getType.html">/sdk-for-flutter-explore-core-metadata-gettype</a>(<wbr/>String key)
    → <a href="../core/MetadataType.html">/sdk-for-flutter-explore-core-metadatatype</a>?

</dt>
<dd>
  Determines the type of a metadata value.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../core/Metadata/noSuchMethod.html">/sdk-for-flutter-explore-core-metadata-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeValue">
<a href="../core/Metadata/removeValue.html">/sdk-for-flutter-explore-core-metadata-removevalue</a>(<wbr/>String key)
    → void

</dt>
<dd>
  Removes a metadata key and its associated value.
  

</dd>
<dt class="callable" id="setCustomValue">
<a href="../core/Metadata/setCustomValue.html">/sdk-for-flutter-explore-core-metadata-setcustomvalue</a>(<wbr/>String key, <a href="../core/CustomMetadataValue-class.html">/sdk-for-flutter-explore-core-custommetadatavalue-class</a> value)
    → void

</dt>
<dd>
  Creates a key:value pair, where the value is a type derived from CustomMetadataValue.
  

</dd>
<dt class="callable" id="setDouble">
<a href="../core/Metadata/setDouble.html">/sdk-for-flutter-explore-core-metadata-setdouble</a>(<wbr/>String key, double value)
    → void

</dt>
<dd>
  Creates a key:value pair, where the value is of type Double.
  

</dd>
<dt class="callable" id="setGeoCoordinates">
<a href="../core/Metadata/setGeoCoordinates.html">/sdk-for-flutter-explore-core-metadata-setgeocoordinates</a>(<wbr/>String key, <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> value)
    → void

</dt>
<dd>
  Creates a key:value pair, where the value is of type GeoCoordinates.
  

</dd>
<dt class="callable" id="setInteger">
<a href="../core/Metadata/setInteger.html">/sdk-for-flutter-explore-core-metadata-setinteger</a>(<wbr/>String key, int value)
    → void

</dt>
<dd>
  Creates a key:value pair, where the value is of type Integer.
  

</dd>
<dt class="callable" id="setString">
<a href="../core/Metadata/setString.html">/sdk-for-flutter-explore-core-metadata-setstring</a>(<wbr/>String key, String value)
    → void

</dt>
<dd>
  Creates a key:value pair, where the value is of type String.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../core/Metadata/toString.html">/sdk-for-flutter-explore-core-metadata-tostring</a>(<wbr/>)
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
<a href="../core/Metadata/operator_equals.html">/sdk-for-flutter-explore-core-metadata-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
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
</HTMLBlock>
