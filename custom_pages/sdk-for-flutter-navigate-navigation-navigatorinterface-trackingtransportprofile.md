---
title: "trackingTransportProfile property"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportprofile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trackingTransportProfile.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">trackingTransportProfile property</li>
</ol>
<div class="self-name">trackingTransportProfile</div>
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
<h1>trackingTransportProfile property</h1></div>
<section id="getter">
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use NavigatorInterface.trackingTransportSpecification instead.")</li>
</ol>
</div>
/sdk-for-flutter-navigate-core-transportprofile-class?
trackingTransportProfile
</section>
<section class="desc markdown">
<p>Defines the transport profile for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.
Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
For example, a /sdk-for-flutter-navigate-core-transportprofile-class can be defined with a /sdk-for-flutter-navigate-transport-vehicleprofile-class.
A vehicle profile can have several parameters such as /sdk-for-flutter-navigate-transport-vehicletype to set the
source of information describing the vehicle.
The default is a /sdk-for-flutter-navigate-transport-vehicletype profile.</p>
<p>Currently used members of /sdk-for-flutter-navigate-core-transportprofile-class</p>
<ul>
<li>/sdk-for-flutter-navigate-transport-vehicletype: Sets the transport mode.</li>
<li>From <code>vehicleProfile</code>:
<ul>
<li><code>grossWeightInKilograms</code>: Required for truck related speed information.</li>
<li><code>heightInCentimeters</code>: Required for truck related speed information.</li>
<li><code>widthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
<li><code>lengthInCentimeters</code>: Additional truck definition for more specific truck speed information.
Gets the transport profile for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.</li>
</ul>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use NavigatorInterface.trackingTransportSpecification instead.")
TransportProfile? get trackingTransportProfile;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use NavigatorInterface.trackingTransportSpecification instead.")</li>
</ol>
</div>
void
trackingTransportProfile=(<wbr/>/sdk-for-flutter-navigate-core-transportprofile-class? value)
</section>
<section class="desc markdown">
<p>Defines the transport profile for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.
Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
For example, a /sdk-for-flutter-navigate-core-transportprofile-class can be defined with a /sdk-for-flutter-navigate-transport-vehicleprofile-class.
A vehicle profile can have several parameters such as /sdk-for-flutter-navigate-transport-vehicletype to set the
source of information describing the vehicle.
The default is a /sdk-for-flutter-navigate-transport-vehicletype profile.</p>
<p>Currently used members of /sdk-for-flutter-navigate-core-transportprofile-class</p>
<ul>
<li>/sdk-for-flutter-navigate-transport-vehicletype: Sets the transport mode.</li>
<li>From <code>vehicleProfile</code>:
<ul>
<li><code>grossWeightInKilograms</code>: Required for truck related speed information.</li>
<li><code>heightInCentimeters</code>: Required for truck related speed information.</li>
<li><code>widthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
<li><code>lengthInCentimeters</code>: Additional truck definition for more specific truck speed information.
Sets the transport profile for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.</li>
</ul>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use NavigatorInterface.trackingTransportSpecification instead.")
set trackingTransportProfile(TransportProfile? value);</code></pre>
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
<li class="self-crumb">trackingTransportProfile property</li>
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
