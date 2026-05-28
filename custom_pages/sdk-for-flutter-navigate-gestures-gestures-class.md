---
title: "Gestures class abstract"
slug: "sdk-for-flutter-navigate-gestures-gestures-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Gestures-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="gestures/Gestures-class.html#constructors">Constructors</a></li>
<li><a href="gestures/Gestures/Gestures.html">Gestures</a></li>
<li class="section-title">
<a href="gestures/Gestures-class.html#instance-properties">Properties</a>
</li>
<li><a href="gestures/Gestures/doubleTapListener.html">doubleTapListener</a></li>
<li class="inherited"><a href="gestures/Gestures/hashCode.html">hashCode</a></li>
<li><a href="gestures/Gestures/longPressListener.html">longPressListener</a></li>
<li><a href="gestures/Gestures/panListener.html">panListener</a></li>
<li><a href="gestures/Gestures/pinchRotateListener.html">pinchRotateListener</a></li>
<li class="inherited"><a href="gestures/Gestures/runtimeType.html">runtimeType</a></li>
<li><a href="gestures/Gestures/tapListener.html">tapListener</a></li>
<li><a href="gestures/Gestures/twoFingerPanListener.html">twoFingerPanListener</a></li>
<li><a href="gestures/Gestures/twoFingerTapListener.html">twoFingerTapListener</a></li>
<li class="section-title"><a href="gestures/Gestures-class.html#instance-methods">Methods</a></li>
<li><a href="gestures/Gestures/disableDefaultAction.html">disableDefaultAction</a></li>
<li><a href="gestures/Gestures/enableDefaultAction.html">enableDefaultAction</a></li>
<li class="inherited"><a href="gestures/Gestures/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="gestures/Gestures/toString.html">toString</a></li>
<li class="section-title inherited"><a href="gestures/Gestures-class.html#operators">Operators</a></li>
<li class="inherited"><a href="gestures/Gestures/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-gestures-gestures-library</li>
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
/sdk-for-flutter-navigate-gestures-gestures-gestures()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="doubleTapListener">
/sdk-for-flutter-navigate-gestures-gestures-doubletaplistener
↔ /sdk-for-flutter-navigate-gestures-doubletaplistener-class?
</dt>
<dd>
/sdk-for-flutter-navigate-gestures-doubletaplistener-class that notifies when a double-tap gesture occurs.
Gets a /sdk-for-flutter-navigate-gestures-doubletaplistener-class that notifies when a double-tap gesture occurs. /sdk-for-flutter-navigate-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-gestures-gestures-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="longPressListener">
/sdk-for-flutter-navigate-gestures-gestures-longpresslistener
↔ /sdk-for-flutter-navigate-gestures-longpresslistener-class?
</dt>
<dd>
/sdk-for-flutter-navigate-gestures-longpresslistener-class that notifies when a long-press gesture occurs.
Gets a /sdk-for-flutter-navigate-gestures-longpresslistener-class that notifies when a long-press gesture occurs. /sdk-for-flutter-navigate-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="panListener">
/sdk-for-flutter-navigate-gestures-gestures-panlistener
↔ /sdk-for-flutter-navigate-gestures-panlistener-class?
</dt>
<dd>
/sdk-for-flutter-navigate-gestures-panlistener-class that notifies when a pan gesture occurs.
Gets a /sdk-for-flutter-navigate-gestures-panlistener-class that notifies when a pan gesture occurs. /sdk-for-flutter-navigate-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pinchRotateListener">
/sdk-for-flutter-navigate-gestures-gestures-pinchrotatelistener
↔ /sdk-for-flutter-navigate-gestures-pinchrotatelistener-class?
</dt>
<dd>
/sdk-for-flutter-navigate-gestures-pinchrotatelistener-class that notifies when a pinch-rotate gesture occurs.
Gets a /sdk-for-flutter-navigate-gestures-pinchrotatelistener-class that notifies when a pinch-rotate gesture occurs. /sdk-for-flutter-navigate-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-gestures-gestures-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tapListener">
/sdk-for-flutter-navigate-gestures-gestures-taplistener
↔ /sdk-for-flutter-navigate-gestures-taplistener-class?
</dt>
<dd>
/sdk-for-flutter-navigate-gestures-taplistener-class that notifies when a tap gesture occurs.
Gets a /sdk-for-flutter-navigate-gestures-taplistener-class that notifies when a tap gesture occurs. /sdk-for-flutter-navigate-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="twoFingerPanListener">
/sdk-for-flutter-navigate-gestures-gestures-twofingerpanlistener
↔ /sdk-for-flutter-navigate-gestures-twofingerpanlistener-class?
</dt>
<dd>
/sdk-for-flutter-navigate-gestures-twofingerpanlistener-class that notifies when a two-finger pan gesture occurs.
Gets a /sdk-for-flutter-navigate-gestures-twofingerpanlistener-class that notifies when a two-finger pan gesture occurs. /sdk-for-flutter-navigate-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="twoFingerTapListener">
/sdk-for-flutter-navigate-gestures-gestures-twofingertaplistener
↔ /sdk-for-flutter-navigate-gestures-twofingertaplistener-class?
</dt>
<dd>
/sdk-for-flutter-navigate-gestures-twofingertaplistener-class that notifies when a two-finger tap gesture occurs.
Gets a /sdk-for-flutter-navigate-gestures-twofingertaplistener-class that notifies when a two-finger tap gesture occurs. /sdk-for-flutter-navigate-gestures-gestures-class holds a strong reference to the listener.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="disableDefaultAction">
/sdk-for-flutter-navigate-gestures-gestures-disabledefaultaction(<wbr/>/sdk-for-flutter-navigate-gestures-gesturetype gestureType)
    → void

</dt>
<dd>
  Disables default action for a specified gesture.
  

</dd>
<dt class="callable" id="enableDefaultAction">
/sdk-for-flutter-navigate-gestures-gestures-enabledefaultaction(<wbr/>/sdk-for-flutter-navigate-gestures-gesturetype gestureType)
    → void

</dt>
<dd>
  Enables default action to be performed for a specified
gesture.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-gestures-gestures-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-gestures-gestures-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-gestures-gestures-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-gestures-gestures-library</li>
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
</div></div>
</div>
`
}</HTMLBlock>
