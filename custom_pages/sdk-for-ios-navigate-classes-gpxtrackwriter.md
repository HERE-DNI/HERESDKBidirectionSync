---
title: "GPXTrackWriter Class Reference"
slug: "sdk-for-ios-navigate-classes-gpxtrackwriter"
---

# GPXTrackWriter

<div class="declaration">

<div class="language">

``` highlight
public class GPXTrackWriter : LocationDelegate
```

``` highlight
extension GPXTrackWriter: NativeBase
```

``` highlight
extension GPXTrackWriter: Hashable
```

</div>

Related types:

- <a href="sdk-for-ios-navigate-protocols-locationdelegate">LocationDelegate</a>

</div>

Writes GPX track points to <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a>. The instance of the class should be added as a listener to the <a href="sdk-for-ios-navigate-classes-locationengine">`LocationEngine`</a> for GPX track recording. Appends the new location to the back segment of the track whenever the listener is called. The following data (if provided) can be recorded and inserted into the resulting <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a>: `latitude, longitude, altitude, time, bearingInDegrees, pitchInDegrees, speedInMetersPerSecond, horizontalAccuracyInMeters, verticalAccuracyInMeters, bearingAccuracyInDegrees, speedAccuracyInMetersPerSecond` and `locationTechnology`.

Use case examples:

A user wants to create and save a new <a href="sdk-for-ios-navigate-classes-gpxdocument">`GPXDocument`</a> with one <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a>:

- create `GPXTrackWriter` and add it as a location listener to <a href="sdk-for-ios-navigate-classes-locationengine">`LocationEngine`</a>.
- set user parameters to <a href="sdk-for-ios-navigate-classes-gpxtrackwriter#sdk-for-ios-navigate-s-7heresdk14GPXTrackWriterC5trackAA0B0Cvp">`GPXTrackWriter.track`</a> (e.g. <a href="sdk-for-ios-navigate-classes-gpxtrack#sdk-for-ios-navigate-s-7heresdk8GPXTrackC4nameSSvp">`GPXTrack.name`</a> or <a href="sdk-for-ios-navigate-classes-gpxtrack#sdk-for-ios-navigate-s-7heresdk8GPXTrackC11descriptionSSvp">`GPXTrack.description`</a>).
- when writing is completed, create a new <a href="sdk-for-ios-navigate-classes-gpxdocument">`GPXDocument`</a> with a list of one <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a> and save the document via <a href="sdk-for-ios-navigate-classes-gpxdocument#sdk-for-ios-navigate-s-7heresdk11GPXDocumentC4save11gpxFilePathSbSS_tF">`GPXDocument.save(...)`</a>.

A user wants to modify and save <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a> in the existing <a href="sdk-for-ios-navigate-classes-gpxdocument">`GPXDocument`</a>:

- load <a href="sdk-for-ios-navigate-classes-gpxdocument">`GPXDocument`</a> from a file by the relevant constructor.
- create `GPXTrackWriter` with the required track in the list <a href="sdk-for-ios-navigate-classes-gpxdocument#sdk-for-ios-navigate-s-7heresdk11GPXDocumentC6tracksSayAA8GPXTrackCGvp">`GPXDocument.tracks`</a>, add the created instance as a location listener to <a href="sdk-for-ios-navigate-classes-locationengine">`LocationEngine`</a>.
- when writing is completed, save the document via <a href="sdk-for-ios-navigate-classes-gpxdocument#sdk-for-ios-navigate-s-7heresdk11GPXDocumentC4save11gpxFilePathSbSS_tF">`GPXDocument.save(...)`</a>.

The <a href="sdk-for-ios-navigate-classes-gpxdocument">`GPXDocument`</a> including all tracks is saved in the <a href="https://www.topografix.com/gpx.asp">GPX</a> file format. Hence, once saved, it can be easily shared with other applications that understand the GPX file format.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14GPXTrackWriterCACycfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gpxtrackwriter#sdk-for-ios-navigate-s-7heresdk14GPXTrackWriterCACycfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of GPXTrackWriter with an empty track inside.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14GPXTrackWriterC5trackAcA0B0C_tcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-track" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gpxtrackwriter#sdk-for-ios-navigate-s-7heresdk14GPXTrackWriterC5trackAcA0B0C_tcfc" class="token"><code>init(track:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of `GPXTrackWriter` with <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a>. Use this constructor to append locations to an existing track.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(track: GPXTrack)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-gpxtrack">GPXTrack</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>track</code></em><code> </code></td>
  <td><div>
  <p>GPX track.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14GPXTrackWriterC5trackAA0B0Cvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-track" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gpxtrackwriter#sdk-for-ios-navigate-s-7heresdk14GPXTrackWriterC5trackAA0B0Cvp" class="token"><code>track</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  GPX track into which GPX track points are written.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var track: GPXTrack { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-gpxtrack">GPXTrack</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14GPXTrackWriterC17onLocationUpdatedyyAA0E0VF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-onLocationUpdated-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-gpxtrackwriter#sdk-for-ios-navigate-s-7heresdk14GPXTrackWriterC17onLocationUpdatedyyAA0E0VF" class="token"><code>onLocationUpdated(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called each time a new location is available. In a navigation context while using the <a href="sdk-for-ios-navigate-classes-navigator">`Navigator`</a> or <a href="sdk-for-ios-navigate-classes-visualnavigator">`VisualNavigator`</a>, it’s required to set the <a href="sdk-for-ios-navigate-structs-location#sdk-for-ios-navigate-s-7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter for each <a href="sdk-for-ios-navigate-structs-location">`Location`</a> object so that the HERE SDK can map-match the locations properly. If the <a href="sdk-for-ios-navigate-structs-location#sdk-for-ios-navigate-s-7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the `bearing` and `speed` parameters for each <a href="sdk-for-ios-navigate-structs-location">`Location`</a> object. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func onLocationUpdated(_ location: Location)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-location">Location</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>location</code></em><code> </code></td>
  <td><div>
  <p>Current location.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

