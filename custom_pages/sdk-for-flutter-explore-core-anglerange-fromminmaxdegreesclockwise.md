---
title: "Implementation"
slug: "sdk-for-flutter-explore-core-anglerange-fromminmaxdegreesclockwise"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- fromMinMaxDegreesClockwise.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li><a href="../../core/AngleRange-class.html">/sdk-for-flutter-explore-core-anglerange-class</a></li>
<li class="self-crumb">fromMinMaxDegreesClockwise static method</li>
</ol>
<div class="self-name">fromMinMaxDegreesClockwise</div>
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
<div class="main-content" data-above-sidebar="core/AngleRange-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>fromMinMaxDegreesClockwise static method</h1></div>
<section class="multi-line-signature">
<a href="../../core/AngleRange-class.html">/sdk-for-flutter-explore-core-anglerange-class</a>
fromMinMaxDegreesClockwise(<wbr/><ol class="parameter-list single-line"> <li>double min, </li>
<li>double max</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Constructs an AngleRange from the provided minimum and maximum angles.</p>
<p>Corrects values if they exceed the ranges. The angles are always
interpreted in clockwise orientation.</p>
<ul>
<li>
<p><code>min</code> Angle where to start the circular sector, running clockwise, in
degrees from north.
The value will be normalized to [0.0, 360.0).</p>
</li>
<li>
<p><code>max</code> Angle where the circular sector ends, running clockwise, in
degrees from north.
The value will be normalized to [0.0, 360.0).</p>
</li>
</ul>
<p>Returns <a href="../../core/AngleRange-class.html">/sdk-for-flutter-explore-core-anglerange-class</a>. Created AngleRange from the provided minimum and maximum angles.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static AngleRange fromMinMaxDegreesClockwise(double min, double max) =&gt; $prototype.fromMinMaxDegreesClockwise(min, max);</code></pre>
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
<li><a href="../../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li><a href="../../core/AngleRange-class.html">/sdk-for-flutter-explore-core-anglerange-class</a></li>
<li class="self-crumb">fromMinMaxDegreesClockwise static method</li>
</ol>
<h5>AngleRange class</h5>
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
