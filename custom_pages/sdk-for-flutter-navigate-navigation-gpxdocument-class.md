---
title: "GPXDocument class abstract"
slug: "sdk-for-flutter-navigate-navigation-gpxdocument-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GPXDocument-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/GPXDocument-class.html#constructors">Constructors</a></li>
<li><a href="navigation/GPXDocument/GPXDocument.html">GPXDocument</a></li>
<li><a href="navigation/GPXDocument/GPXDocument.withTracks.html">withTracks</a></li>
<li class="section-title">
<a href="navigation/GPXDocument-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="navigation/GPXDocument/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="navigation/GPXDocument/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/GPXDocument/tracks.html">tracks</a></li>
<li class="section-title"><a href="navigation/GPXDocument-class.html#instance-methods">Methods</a></li>
<li><a href="navigation/GPXDocument/addTrack.html">addTrack</a></li>
<li class="inherited"><a href="navigation/GPXDocument/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="navigation/GPXDocument/save.html">save</a></li>
<li class="inherited"><a href="navigation/GPXDocument/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/GPXDocument-class.html#operators">Operators</a></li>
<li class="inherited"><a href="navigation/GPXDocument/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="navigation/GPXDocument-class.html#static-methods">Static methods</a></li>
<li><a href="navigation/GPXDocument/fromString.html">fromString</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">GPXDocument class</li>
</ol>
<div class="self-name">GPXDocument</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/GPXDocument-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>GPXDocument class abstract</h1></div>
<section class="desc markdown">
<p>Use the GPXDocument to load the GPX file.</p>
<p>Only track data is used from the GPX file format
(see trkType at <a href="https://www.topografix.com/GPX/1/1/#type_trkType">https://www.topografix.com/GPX/1/1/#type_trkType</a>).
Any unknown elements in the file are ignored.
Any known element with an invalid value returns an error.
Elevation values are ignored.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="GPXDocument">
/sdk-for-flutter-navigate-navigation-gpxdocument-gpxdocument(String gpxFilePath, /sdk-for-flutter-navigate-navigation-gpxoptions-class options)
</dt>
<dd>
          Create a GPX document from a file.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="GPXDocument.withTracks">
/sdk-for-flutter-navigate-navigation-gpxdocument-gpxdocument-withtracks(List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-gpxtrack-class&gt; tracks)
</dt>
<dd>
          Create a GPX document from a list of GPX tracks.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-gpxdocument-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-gpxdocument-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tracks">
/sdk-for-flutter-navigate-navigation-gpxdocument-tracks
→ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-gpxtrack-class&gt;
</dt>
<dd>
  The tracks stored in this GPX document.
Gets the tracks stored in this GPX document.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addTrack">
/sdk-for-flutter-navigate-navigation-gpxdocument-addtrack(<wbr/>/sdk-for-flutter-navigate-navigation-gpxtrack-class trackToAdd)
    → void

</dt>
<dd>
  Add track to GPX document.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-gpxdocument-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="save">
/sdk-for-flutter-navigate-navigation-gpxdocument-save(<wbr/>String gpxFilePath)
    → bool

</dt>
<dd>
  Saves the document to a file.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-gpxdocument-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-gpxdocument-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="fromString">
/sdk-for-flutter-navigate-navigation-gpxdocument-fromstring(<wbr/>String content, /sdk-for-flutter-navigate-navigation-gpxoptions-class options)
    → /sdk-for-flutter-navigate-navigation-gpxdocument-class

</dt>
<dd>
  Create a GPX document from a string.
  

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
<li class="self-crumb">GPXDocument class</li>
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
