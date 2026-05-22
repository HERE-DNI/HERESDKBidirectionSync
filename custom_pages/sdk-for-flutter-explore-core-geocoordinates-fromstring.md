---
title: "Untitled"
slug: "sdk-for-flutter-explore-core-geocoordinates-fromstring"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fromString.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li>/sdk-for-flutter-explore-core-geocoordinates-class</li>
<li class="self-crumb">fromString static method</li>
</ol>
<div class="self-name">fromString</div>
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
<div class="main-content" data-above-sidebar="core/GeoCoordinates-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>fromString static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-core-geocoordinates-class?
fromString(<wbr/><ol class="parameter-list single-line"> <li>String input</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Constructs GeoCoordinates from the provided string in specified format.</p>
<p>Corrects values of lat and long if they exceed the ranges.
If the latitude value is out of range of [-90.0, 90.0] it's clamped to that range.
If the longitude value is out of range of [-180.0, 180.0] it's replaced with a value
within the range, representing effectively the same meridian.
Examples: <code>53.43762,-13.65468</code>.
<code>49°59'56.948"N, 15°48'22.989"E</code>
<code>50d4m17.698N 14d24m2.826E</code>
<code>49.9991522N, 150.8063858E</code>
<code>40°26′47″N 79°58′36″W</code></p>
<ul>
<li><code>input</code> String representing GeoCoordinates in one of supported formats.</li>
</ul>
<p>Returns /sdk-for-flutter-explore-core-geocoordinates-class. Created GeoCoordinates, or 'null' if string was not in appropriate format.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static GeoCoordinates? fromString(String input) =&gt; $prototype.fromString(input);</code></pre>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li>/sdk-for-flutter-explore-core-geocoordinates-class</li>
<li class="self-crumb">fromString static method</li>
</ol>
<h5>GeoCoordinates class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
