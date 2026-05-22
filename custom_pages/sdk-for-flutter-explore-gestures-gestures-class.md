---
title: "Untitled"
slug: "sdk-for-flutter-explore-gestures-gestures-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Gestures-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-gestures-gestures-library</li>
<li class="self-crumb">Gestures class</li>
</ol>
<div class="self-name">Gestures</div>
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
<div class="main-content" data-above-sidebar="gestures/gestures-library-sidebar.html" data-below-sidebar="gestures/Gestures-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Gestures class abstract</h1></div>
<section class="desc markdown">
<p>Use this class to process touch events from the platform and detect gesture induced actions on the map view.</p>
<p>Please note that this class holds strong references to the gesture listeners.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Gestures">
/sdk-for-flutter-explore-gestures-gestures-gestures()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="doubleTapListener">
/sdk-for-flutter-explore-gestures-gestures-doubletaplistener
↔ /sdk-for-flutter-explore-gestures-doubletaplistener-class?
</dt>
<dd>
/sdk-for-flutter-explore-gestures-doubletaplistener-class that notifies when a double-tap gesture occurs.
Gets a /sdk-for-flutter-explore-gestures-doubletaplistener-class that notifies when a double-tap gesture occurs. /sdk-for-flutter-explore-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-gestures-gestures-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="longPressListener">
/sdk-for-flutter-explore-gestures-gestures-longpresslistener
↔ /sdk-for-flutter-explore-gestures-longpresslistener-class?
</dt>
<dd>
/sdk-for-flutter-explore-gestures-longpresslistener-class that notifies when a long-press gesture occurs.
Gets a /sdk-for-flutter-explore-gestures-longpresslistener-class that notifies when a long-press gesture occurs. /sdk-for-flutter-explore-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="panListener">
/sdk-for-flutter-explore-gestures-gestures-panlistener
↔ /sdk-for-flutter-explore-gestures-panlistener-class?
</dt>
<dd>
/sdk-for-flutter-explore-gestures-panlistener-class that notifies when a pan gesture occurs.
Gets a /sdk-for-flutter-explore-gestures-panlistener-class that notifies when a pan gesture occurs. /sdk-for-flutter-explore-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pinchRotateListener">
/sdk-for-flutter-explore-gestures-gestures-pinchrotatelistener
↔ /sdk-for-flutter-explore-gestures-pinchrotatelistener-class?
</dt>
<dd>
/sdk-for-flutter-explore-gestures-pinchrotatelistener-class that notifies when a pinch-rotate gesture occurs.
Gets a /sdk-for-flutter-explore-gestures-pinchrotatelistener-class that notifies when a pinch-rotate gesture occurs. /sdk-for-flutter-explore-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-gestures-gestures-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tapListener">
/sdk-for-flutter-explore-gestures-gestures-taplistener
↔ /sdk-for-flutter-explore-gestures-taplistener-class?
</dt>
<dd>
/sdk-for-flutter-explore-gestures-taplistener-class that notifies when a tap gesture occurs.
Gets a /sdk-for-flutter-explore-gestures-taplistener-class that notifies when a tap gesture occurs. /sdk-for-flutter-explore-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="twoFingerPanListener">
/sdk-for-flutter-explore-gestures-gestures-twofingerpanlistener
↔ /sdk-for-flutter-explore-gestures-twofingerpanlistener-class?
</dt>
<dd>
/sdk-for-flutter-explore-gestures-twofingerpanlistener-class that notifies when a two-finger pan gesture occurs.
Gets a /sdk-for-flutter-explore-gestures-twofingerpanlistener-class that notifies when a two-finger pan gesture occurs. /sdk-for-flutter-explore-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="twoFingerTapListener">
/sdk-for-flutter-explore-gestures-gestures-twofingertaplistener
↔ /sdk-for-flutter-explore-gestures-twofingertaplistener-class?
</dt>
<dd>
/sdk-for-flutter-explore-gestures-twofingertaplistener-class that notifies when a two-finger tap gesture occurs.
Gets a /sdk-for-flutter-explore-gestures-twofingertaplistener-class that notifies when a two-finger tap gesture occurs. /sdk-for-flutter-explore-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="disableDefaultAction">
/sdk-for-flutter-explore-gestures-gestures-disabledefaultaction(<wbr/>/sdk-for-flutter-explore-gestures-gesturetype gestureType)
    → void

</dt>
<dd>
  Disables default action for a specified gesture.
  

</dd>
<dt class="callable" id="enableDefaultAction">
/sdk-for-flutter-explore-gestures-gestures-enabledefaultaction(<wbr/>/sdk-for-flutter-explore-gestures-gesturetype gestureType)
    → void

</dt>
<dd>
  Enables default action to be performed for a specified
gesture.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-gestures-gestures-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-gestures-gestures-tostring(<wbr/>)
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
/sdk-for-flutter-explore-gestures-gestures-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-gestures-gestures-library</li>
<li class="self-crumb">Gestures class</li>
</ol>
<h5>gestures library</h5>
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
