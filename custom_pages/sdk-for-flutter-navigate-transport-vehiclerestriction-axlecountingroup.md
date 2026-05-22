---
title: "Untitled"
slug: "sdk-for-flutter-navigate-transport-vehiclerestriction-axlecountingroup"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- axleCountInGroup.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li>/sdk-for-flutter-navigate-transport-vehiclerestriction-class</li>
<li class="self-crumb">axleCountInGroup property</li>
</ol>
<div class="self-name">axleCountInGroup</div>
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
<div class="main-content" data-above-sidebar="transport/VehicleRestriction-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>axleCountInGroup property</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-integerrange-class?
        axleCountInGroup
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Number of axles in a group for which the current restriction applies.
<code>axleCountInGroup</code> is a set of axles close together: single, tandem (2), triple (3), etc.
Can be used in conjunction with /sdk-for-flutter-navigate-transport-restrictiontype
to specify restriction based on weight per axle group.
The <code>axleCountInGroup</code> considers number of axles in a specific axle group (usually rear axles on the truck or trailer).
This can be used to limit weight for a tandem/triple rear axle group.
If the upper limit of the <code>axleCountInGroup</code> range is 0 or <code>null</code> then it means the restriction applies
for values &gt;= lower limit, i.e. the upper limit of range if infinite or unbound.
Examples:</p>
<ul>
<li>(1,1) → Restriction applies to single axle group.</li>
<li>(2,2) → Restriction applies to tandem axle group.</li>
<li>(2,4) → Restriction applies to any axle group from 2 to 4 axles.</li>
<li>(2,0) → Restriction applies to axle groups with 2 or more axles.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">IntegerRange? axleCountInGroup;</code></pre>
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
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li>/sdk-for-flutter-navigate-transport-vehiclerestriction-class</li>
<li class="self-crumb">axleCountInGroup property</li>
</ol>
<h5>VehicleRestriction class</h5>
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
