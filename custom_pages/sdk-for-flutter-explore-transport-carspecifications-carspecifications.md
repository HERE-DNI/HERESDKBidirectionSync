---
title: "Implementation"
slug: "sdk-for-flutter-explore-transport-carspecifications-carspecifications"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- CarSpecifications.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../transport/transport-library.html">/sdk-for-flutter-explore-transport-transport-library</a></li>
<li><a href="../../transport/CarSpecifications-class.html">/sdk-for-flutter-explore-transport-carspecifications-class</a></li>
<li class="self-crumb">CarSpecifications constructor</li>
</ol>
<div class="self-name">CarSpecifications</div>
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
<div class="main-content" data-above-sidebar="transport/CarSpecifications-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>CarSpecifications constructor</h1></div>
<section class="multi-line-signature">
CarSpecifications(<wbr/>[<ol class="parameter-list"> <li>int? grossWeightInKilograms = null, </li>
<li>int? heightInCentimeters = null, </li>
<li>int? widthInCentimeters = null, </li>
<li>int? lengthInCentimeters = null, </li>
<li>int? axleCount = null, </li>
<li>int? trailerCount = null, </li>
<li>int? trailerAxleCount = null, </li>
</ol>])
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>grossWeightInKilograms</code> Car weight including trailers and shipped goods in kilograms. The provided value
must be greater than or equal to 0. By default, it is not set.
<strong>Note:</strong>
This parameter is limited to a maximum weight of 4250 kg without trailer and 7550 kg with trailer.</li>
<li><code>heightInCentimeters</code> Car height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
<li><code>widthInCentimeters</code> Car width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
<li><code>lengthInCentimeters</code> Car length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.</li>
<li><code>axleCount</code> Defines total number of axles in the vehicle. The provided value must be greater than or
equal to 2. By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be
taken into consideration.
When specifying <a href="../../transport/CarSpecifications/trailerAxleCount.html">/sdk-for-flutter-explore-transport-carspecifications-traileraxlecount</a>, then <a href="../../transport/CarSpecifications/axleCount.html">/sdk-for-flutter-explore-transport-carspecifications-axlecount</a> is required and must be greater than <a href="../../transport/CarSpecifications/trailerAxleCount.html">/sdk-for-flutter-explore-transport-carspecifications-traileraxlecount</a>.</li>
<li><code>trailerCount</code> Defines number of trailers attached to the vehicle. The provided value must be in the range
[0, 1]. By default, it is not set.
When specifying <a href="../../transport/CarSpecifications/trailerAxleCount.html">/sdk-for-flutter-explore-transport-carspecifications-traileraxlecount</a>, then <a href="../../transport/CarSpecifications/trailerCount.html">/sdk-for-flutter-explore-transport-carspecifications-trailercount</a> is required and must be greater than 0.</li>
<li><code>trailerAxleCount</code> Defines total number of axles across all the trailers attached to the vehicle.
This number is included in <a href="../../transport/CarSpecifications/axleCount.html">/sdk-for-flutter-explore-transport-carspecifications-axlecount</a>, hence <a href="../../transport/CarSpecifications/trailerAxleCount.html">/sdk-for-flutter-explore-transport-carspecifications-traileraxlecount</a> must be less than <a href="../../transport/CarSpecifications/axleCount.html">/sdk-for-flutter-explore-transport-carspecifications-axlecount</a>
and greater than or equal to 1. <a href="../../transport/CarSpecifications/axleCount.html">/sdk-for-flutter-explore-transport-carspecifications-axlecount</a> and <a href="../../transport/CarSpecifications/trailerCount.html">/sdk-for-flutter-explore-transport-carspecifications-trailercount</a> are required to specify <a href="../../transport/CarSpecifications/trailerAxleCount.html">/sdk-for-flutter-explore-transport-carspecifications-traileraxlecount</a>.
By default, it is not set.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">CarSpecifications([int? grossWeightInKilograms = null, int? heightInCentimeters = null, int? widthInCentimeters = null, int? lengthInCentimeters = null, int? axleCount = null, int? trailerCount = null, int? trailerAxleCount = null])
  : grossWeightInKilograms = grossWeightInKilograms, heightInCentimeters = heightInCentimeters, widthInCentimeters = widthInCentimeters, lengthInCentimeters = lengthInCentimeters, axleCount = axleCount, trailerCount = trailerCount, trailerAxleCount = trailerAxleCount;</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../transport/transport-library.html">/sdk-for-flutter-explore-transport-transport-library</a></li>
<li><a href="../../transport/CarSpecifications-class.html">/sdk-for-flutter-explore-transport-carspecifications-class</a></li>
<li class="self-crumb">CarSpecifications constructor</li>
</ol>
<h5>CarSpecifications class</h5>
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
