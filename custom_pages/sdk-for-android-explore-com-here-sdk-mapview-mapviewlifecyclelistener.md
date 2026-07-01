---
title: "MapViewLifecycleListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapviewlifecyclelistener"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface
</span><span class="element-name type-name-label">MapViewLifecycleListener</span>

</div>

<div class="block">

Provides a mechanism for observing a lifecycle of a map view and/or
implementing components whose lifecycle needs to be linked with that of
a map view. A configuration change that results in Activity being
recreated does not trigger an onDestroy() call. The listener will be
preserved throughout the destruction and recreation of the MapView. It
is safe to hold and use the MapViewBase object passed in
onAttach(com.here.sdk.mapview.MapViewBase) until onDetach() or
onDestroy() gets called. However, it is important that the listener does
not hold a strong reference to an Activity , directly or indirectly (for
example by holding a reference to a MapView . A component implementing
this interface should interact with the map view only through the
MapViewBase object passed in onAttach(com.here.sdk.mapview.MapViewBase)
. A MapView is using a SurfaceView to render its content.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onAttach(MapViewBase mapView)</code></pre></td>
  <td><div class="block">
  Called when adding MapViewLifecycleListener to the map view.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onDestroy()</code></pre></td>
  <td><div class="block">
  Called when the map view to which this is attached to is destroyed.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onDetach(MapViewBase mapView)</code></pre></td>
  <td><div class="block">
  Called when removing MapViewLifecycleListener from the map view.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onPause()</code></pre></td>
  <td><div class="block">
  Called when the map view to which this MapViewLifecycleListener is
  attached to gets paused (usually when the app goes into background).
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onResume()</code></pre></td>
  <td><div class="block">
  Called when the map view to which this MapViewLifecycleListener is
  attached to gets resumed (usually when the app goes into foreground).
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="onAttach(com.here.sdk.mapview.MapViewBase)"
    class="section detail">

    ### onAttach

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onAttach</span><span class="parameters">(@NonNull
    [MapViewBase](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview") mapView)</span>

    </div>

    <div class="block">

    Called when adding MapViewLifecycleListener to the map view. If the
    map view does not have render target attached at the time of adding
    the listener, then this method will be called later, after render
    target is attached. This means that the map view it receives is
    always fully initialized. Can be used to implement the logic to
    create and add visual components to the map view.

    </div>

    Parameters:  
    `mapView` -

    The map view to attach to.

    </div>

  - <div id="onDetach(com.here.sdk.mapview.MapViewBase)"
    class="section detail">

    ### onDetach

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onDetach</span><span class="parameters">(@NonNull
    [MapViewBase](sdk-for-android-explore-com-here-sdk-mapview-mapviewbase "interface in com.here.sdk.mapview") mapView)</span>

    </div>

    <div class="block">

    Called when removing MapViewLifecycleListener from the map view. Can
    be used to implement the logic to remove visual components from the
    map view and release resources if necessary.

    </div>

    Parameters:  
    `mapView` -

    The map view to detach from.

    </div>

  - <div id="onPause()" class="section detail">

    ### onPause

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onPause</span>()

    </div>

    <div class="block">

    Called when the map view to which this MapViewLifecycleListener is
    attached to gets paused (usually when the app goes into background).
    This should be used by components that perform continuous updates to
    pause those updates until onResume() is called.

    </div>

    </div>

  - <div id="onResume()" class="section detail">

    ### onResume

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onResume</span>()

    </div>

    <div class="block">

    Called when the map view to which this MapViewLifecycleListener is
    attached to gets resumed (usually when the app goes into
    foreground). This should be used by components that perform
    continuous updates to resume those updates after a previous call to
    onPause() .

    </div>

    </div>

  - <div id="onDestroy()" class="section detail">

    ### onDestroy

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onDestroy</span>()

    </div>

    <div class="block">

    Called when the map view to which this is attached to is destroyed.
    After this is called, no other MapViewLifecycleListener method will
    be invoked. This should be used to make sure all resources are
    freed.

    </div>

    </div>

  </div>

</div>

