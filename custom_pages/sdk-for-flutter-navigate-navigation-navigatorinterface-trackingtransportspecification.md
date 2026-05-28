---
title: "trackingTransportSpecification property"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trackingTransportSpecification.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">trackingTransportSpecification property</li>
</ol>
<div class="self-name">trackingTransportSpecification</div>
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
<div class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>trackingTransportSpecification property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-navigate-transport-transportspecification-class?
trackingTransportSpecification
</section>
<section class="desc markdown">
<p>Defines the transport specification for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.
Properly setting the transport specification optimizes the navigation experience, and improves
resource consumption. An /sdk-for-flutter-navigate-transport-transportspecification-class must have the /sdk-for-flutter-navigate-transport-transportspecification-transportmode set.
A transport specification can have several parameters defined such as /sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters
defined in /sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification to set the source of information describing the vehicle.
By default the /sdk-for-flutter-navigate-transport-transportspecification-class will have the transport mode set to /sdk-for-flutter-navigate-transport-transportmode.</p>
<p>Currently used members of /sdk-for-flutter-navigate-transport-transportspecification-class</p>
<ul>
<li>/sdk-for-flutter-navigate-transport-transportspecification-transportmode: Sets the transport mode.</li>
<li>From /sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification:
<ul>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms: Required for truck related speed information.</li>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters: Required for truck related speed information.</li>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters: Additional truck definition for more specific truck speed information.</li>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters: Additional truck definition for more specific truck speed information.
Gets the transport specification for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.</li>
</ul>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TransportSpecification? get trackingTransportSpecification;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
trackingTransportSpecification=(<wbr/>/sdk-for-flutter-navigate-transport-transportspecification-class? value)
</section>
<section class="desc markdown">
<p>Defines the transport specification for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.
Properly setting the transport specification optimizes the navigation experience, and improves
resource consumption. An /sdk-for-flutter-navigate-transport-transportspecification-class must have the /sdk-for-flutter-navigate-transport-transportspecification-transportmode set.
A transport specification can have several parameters defined such as /sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters
defined in /sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification to set the source of information describing the vehicle.
By default the /sdk-for-flutter-navigate-transport-transportspecification-class will have the transport mode set to /sdk-for-flutter-navigate-transport-transportmode.</p>
<p>Currently used members of /sdk-for-flutter-navigate-transport-transportspecification-class</p>
<ul>
<li>/sdk-for-flutter-navigate-transport-transportspecification-transportmode: Sets the transport mode.</li>
<li>From /sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification:
<ul>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms: Required for truck related speed information.</li>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters: Required for truck related speed information.</li>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters: Additional truck definition for more specific truck speed information.</li>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters: Additional truck definition for more specific truck speed information.
Sets the transport specification for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.</li>
</ul>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set trackingTransportSpecification(TransportSpecification? value);</code></pre>
</section>
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
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">trackingTransportSpecification property</li>
</ol>
<h5>NavigatorInterface class</h5>
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
