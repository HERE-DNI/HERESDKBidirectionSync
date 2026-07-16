---
title: "SpatialAudioCuePanning Class Reference"
slug: "sdk-for-ios-explore-classes-spatialaudiocuepanning"
---

# SpatialAudioCuePanning

<div class="declaration">

<div class="language">

``` highlight
public class SpatialAudioCuePanning
```

``` highlight
extension SpatialAudioCuePanning: NativeBase
```

``` highlight
extension SpatialAudioCuePanning: Hashable
```

</div>

</div>

Use the `SpatialAudioCuePanning` to notify each of the azimuths which compose a spatial audio trajectory along the audio cue.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22SpatialAudioCuePanningC02onB21AzimuthStarterHandlera"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-onSpatialAzimuthStarterHandler" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-spatialaudiocuepanning#sdk-for-ios-explore-s-7heresdk22SpatialAudioCuePanningC02onB21AzimuthStarterHandlera" class="token"><code>onSpatialAzimuthStarterHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called once

      startAngularPanning()

  starts.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias onSpatialAzimuthStarterHandler = (_ spatialTrajectoryData: SpatialTrajectoryData) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-spatialtrajectorydata">SpatialTrajectoryData</a>

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
  <td><code> </code><em><code>spatialTrajectoryData</code></em><code> </code></td>
  <td><div>
  <p>The angular panning information of the current spatial trajectory.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22SpatialAudioCuePanningC012startAngularE0010nextCustomE4Data15azimuthCallbackyAA0ieJ0VSg_yAA0b10TrajectoryJ0VctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-startAngularPanning-nextCustomPanningData-azimuthCallback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-spatialaudiocuepanning#sdk-for-ios-explore-s-7heresdk22SpatialAudioCuePanningC012startAngularE0010nextCustomE4Data15azimuthCallbackyAA0ieJ0VSg_yAA0b10TrajectoryJ0VctF" class="token"><code>startAngularPanning(nextCustomPanningData:</code><wbr></wbr><code>azimuthCallback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method will retrieve a stream of azimuth values to be passed onto the spatial audio renderer. An optional custom value for <a href="sdk-for-ios-explore-structs-custompanningdata#sdk-for-ios-explore-s-7heresdk17CustomPanningDataV25estimatedAudioCueDurationSdSgvp">`CustomPanningData.estimatedAudioCueDuration`</a>, <a href="sdk-for-ios-explore-structs-custompanningdata#sdk-for-ios-explore-s-7heresdk17CustomPanningDataV23initialAzimuthInDegreesSdSgvp">`CustomPanningData.initialAzimuthInDegrees`</a>, or its <a href="sdk-for-ios-explore-structs-custompanningdata#sdk-for-ios-explore-s-7heresdk17CustomPanningDataV21sweepAzimuthInDegreesSdSgvp">`CustomPanningData.sweepAzimuthInDegrees`</a> can be here defined if the default data does not fully match the utilized Language or TTS engine or angle expectations. If startAngularPanning is called to spatialize the audio cue of a new maneuver before the full completion of a previous spatial audio trajectory, then <a href="sdk-for-ios-explore-protocols-eventtextdelegate">`EventTextDelegate`</a> will retrieve the azimuth values of the new maneuver.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func startAngularPanning(nextCustomPanningData: CustomPanningData?, azimuthCallback: @escaping SpatialAudioCuePanning.onSpatialAzimuthStarterHandler)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-custompanningdata">CustomPanningData</a>
  - <a href="sdk-for-ios-explore-classes-spatialaudiocuepanning#sdk-for-ios-explore-s-7heresdk22SpatialAudioCuePanningC02onB21AzimuthStarterHandlera">onSpatialAzimuthStarterHandler</a>

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
  <td><code> </code><em><code>nextCustomPanningData</code></em><code> </code></td>
  <td><div>
  <p>Defines a new set of values related to spatial audio panning. When <a href="sdk-for-ios-explore-structs-custompanningdata"><code>CustomPanningData</code></a> is initialized as <code>nil</code>, the default set of values provided by HERE SDK will be used instead.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>azimuthCallback</code></em><code> </code></td>
  <td><div>
  <p>Callback that will signal the next azimuth required to complete a spatial audio trajectory once the angular panning has started. Azimuth angular values are retrieved individually until the full duration of the audio trajectory has been reached, or a new text message has started its angular panning.</p>
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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

