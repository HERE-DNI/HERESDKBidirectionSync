---
title: "Implementation"
slug: "sdk-for-flutter-explore-transport-truckspecifications-istrucklight"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- isTruckLight.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../transport/transport-library.html">/sdk-for-flutter-explore-transport-transport-library</a></li>
<li><a href="../../transport/TruckSpecifications-class.html">/sdk-for-flutter-explore-transport-truckspecifications-class</a></li>
<li class="self-crumb">isTruckLight property</li>
</ol>
<div class="self-name">isTruckLight</div>
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
<div class="main-content" data-above-sidebar="transport/TruckSpecifications-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>isTruckLight property</h1></div>
<section class="multi-line-signature">
        
        bool
        isTruckLight
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
The flag should not be set to <code>true</code> in other countries than Japan. The flag defaults to <code>false</code>.</p>
<p>A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets
the vehicle can access, which access restrictions apply, and which speed limits are applicable.
Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will
not always overwrite these settings: Make sure to not exceed the specifications that classify a truck as light.</p>
<p>In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to true,
you will get, for example, the same speed limits as for cars. Make sure to set the flag only to true, when
a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.</p>
<p>When <code>TruckSpecifications</code> are set as part of <code>MapContentSettings</code>, then this flag will be ignored and
has no effect.</p>
<p><strong>Note:</strong>
This flag and the concept of light trucks are supported only in Japan as beta and are considered to be
experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.
Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases with a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool isTruckLight;</code></pre>
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
<li><a href="../../transport/TruckSpecifications-class.html">/sdk-for-flutter-explore-transport-truckspecifications-class</a></li>
<li class="self-crumb">isTruckLight property</li>
</ol>
<h5>TruckSpecifications class</h5>
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
