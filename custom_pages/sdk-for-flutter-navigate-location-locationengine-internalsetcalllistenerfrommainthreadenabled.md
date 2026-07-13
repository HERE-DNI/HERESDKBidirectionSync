---
title: "internalsetCallListenerFromMainThreadEnabled method - LocationEngine class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationengine-internalsetcalllistenerfrommainthreadenabled"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/LocationEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">internalsetCallListenerFromMainThreadEnabled</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">internalsetCallListenerFromMainThreadEnabled</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-internalsetCallListenerFromMainThreadEnabled-param-enabled" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enabled</span></span>

)

</div>

<div class="section desc markdown">

Enables or disables forcing listener calls to originate from main thread.

When disabled listener calls can originate from any thread. Defaults to false .

For internal use only.

- `enabled` The enabled flag.

@nodoc

</div>

## Implementation

``` dart
void internalsetCallListenerFromMainThreadEnabled(bool enabled) =>
    _location.internalsetCallListenerFromMainThreadEnabled(enabled);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

