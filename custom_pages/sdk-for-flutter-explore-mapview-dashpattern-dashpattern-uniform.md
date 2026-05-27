---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-dashpattern-dashpattern-uniform"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- DashPattern.uniform.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/DashPattern-class.html">/sdk-for-flutter-explore-mapview-dashpattern-class</a></li>
<li class="self-crumb">DashPattern.uniform factory constructor</li>
</ol>
<div class="self-name">DashPattern.uniform</div>
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
<div class="main-content" data-above-sidebar="mapview/DashPattern-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>DashPattern.uniform constructor</h1></div>
<section class="multi-line-signature">
DashPattern.uniform(<wbr/><ol class="parameter-list single-line"> <li>double dashLength</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a uniform dash pattern in which the length of a gap is the same
as the length of a dash.</p>
<p>This allows for patterns like <code>' — — — —'</code> or <code>'   ———   ———   ———'</code>.</p>
<ul>
<li><code>dashLength</code> The length of a dash in pixels. The gap will have the same length.
Clamped to the range of [1, 500].</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DashPattern.uniform(double dashLength) =&gt; $prototype.uniform(dashLength);</code></pre>
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
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/DashPattern-class.html">/sdk-for-flutter-explore-mapview-dashpattern-class</a></li>
<li class="self-crumb">DashPattern.uniform factory constructor</li>
</ol>
<h5>DashPattern class</h5>
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
