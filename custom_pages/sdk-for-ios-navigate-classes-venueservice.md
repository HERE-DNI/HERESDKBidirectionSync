---
title: "VenueService Class Reference"
slug: "sdk-for-ios-navigate-classes-venueservice"
---

# VenueService

<div class="declaration">

<div class="language">

``` highlight
public class VenueService
```

``` highlight
extension VenueService: NativeBase
```

``` highlight
extension VenueService: Hashable
```

</div>

</div>

Offers methods to download venues. Use of this object does not necessitate Map involvement.

Before loading the venues, initialize the venue service with one of the start methods.

The venue service is online only. Even if there is a cached venue on the device, the venue service requires an online connection to check if the venue is available for the user.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk12VenueServiceC10Int32Arraya"></span>` `<span id="//apple_ref/swift/Alias/Int32Array" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venueservice#/s:7heresdk12VenueServiceC10Int32Arraya" class="token"><code>Int32Array</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias Int32Array = [Int32]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueServiceC11StringArraya"></span>` `<span id="//apple_ref/swift/Alias/StringArray" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venueservice#/s:7heresdk12VenueServiceC11StringArraya" class="token"><code>StringArray</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias StringArray = [String]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueServiceC0B8InfoLista"></span>` `<span id="//apple_ref/swift/Alias/VenueInfoList" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venueservice#/s:7heresdk12VenueServiceC0B8InfoLista" class="token"><code>VenueInfoList</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias VenueInfoList = [VenueInfo]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueServiceC0B19OptionalFeatureLista"></span>` `<span id="//apple_ref/swift/Alias/VenueOptionalFeatureList" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venueservice#/s:7heresdk12VenueServiceC0B19OptionalFeatureLista" class="token"><code>VenueOptionalFeatureList</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias VenueOptionalFeatureList = [VenueService.VenueOptionalFeature]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueServiceC9languagesSaySSGvp"></span>` `<span id="//apple_ref/swift/Property/languages" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venueservice#/s:7heresdk12VenueServiceC9languagesSaySSGvp" class="token"><code>languages</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The languages available in the venue service.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var languages: VenueService.StringArray { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueServiceC8languageSSvp"></span>` `<span id="//apple_ref/swift/Property/language" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venueservice#/s:7heresdk12VenueServiceC8languageSSvp" class="token"><code>language</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The active language. The venue service will try to load a venue with a translation in the active language. If such translation doesn’t exist, a venue will be loaded in its default language.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var language: String { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueServiceC0B15OptionalFeatureO"></span>` `<span id="//apple_ref/swift/Enum/VenueOptionalFeature" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venueservice#/s:7heresdk12VenueServiceC0B15OptionalFeatureO" class="token"><code>VenueOptionalFeature</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional features enum

  <a href="sdk-for-ios-navigate-classes-venueservice-venueoptionalfeature" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum VenueOptionalFeature : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      stop()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Stops the venue service.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func stop ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      addServiceDelegate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a service delegate. The delegate is not added if it is `nil` or is already present in the list of delegates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addServiceDelegate ( _ delegate : VenueServiceDelegate )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The service delegate to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeServiceDelegate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a service delegate. The delegate is not removed if it is not present in the list of delegates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeServiceDelegate ( _ delegate : VenueServiceDelegate )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The service delegate to remove.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addVenueDelegate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a venue delegate. The delegate is not added if it is `nil` or is already present in the list of delegates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueDelegate ( _ delegate : VenueDelegate )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The venue delegate to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeVenueDelegate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a venue delegate. The delegate is not removed if it is not present in the list of delegates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeVenueDelegate ( _ delegate : VenueDelegate )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The venue delegate to remove.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addVenueMapDelegate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a venue map delegate. The delegate is not added if it is `nil` or is already present in the list of delegates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueMapDelegate ( _ delegate : VenueMapDelegate )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The venue map delegate to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeVenueMapDelegate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a venue map delegate. The delegate is not removed if it is not present in the list of delegates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeVenueMapDelegate ( _ delegate : VenueMapDelegate )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The venue map delegate to remove.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      getInitStatus()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets an initialization status.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getInitStatus () -> VenueServiceInitStatus
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  The initialization status.

  </div>

  </div>

  </div>

- <div>

      isInitialized()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Checks if the venue service is initialized.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func isInitialized () -> Bool
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  `True` if the venue service is initialized and `false` otherwise.

  </div>

  </div>

  </div>

- <div>

      addVenueToLoad(venueId: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a venue to the loading queue.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueToLoad ( venueId : Int32 )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>venueId</code></em><code> </code></td>
  <td><div>
  <p>The id of the venue to load.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addVenueToLoad(venueIdentifier: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a venue to the loading queue.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueToLoad ( venueIdentifier : String )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>venueIdentifier</code></em><code> </code></td>
  <td><div>
  <p>The id of the venue to load.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      setHrn(hrn: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets HRN of platform catalog.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setHrn ( hrn : String )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>hrn</code></em><code> </code></td>
  <td><div>
  <p>The HRN of platform catalog.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      setLabeltextPreference(labelTextPref: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets override labelTextPreference for labels.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setLabeltextPreference ( labelTextPref : [ String ])
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>labelTextPref</code></em><code> </code></td>
  <td><div>
  <p>The list of string override labelTextPreference.</p>
  <p>“OCCUPANT_NAMES” - To display only occupant names on map as a label text. Example: Boutique Du Chocolat for id 7348</p>
  <p>“SPACE_NAME” - To display only space names on map as a label text. Example: Family Services/First Aid for id 7348</p>
  <p>“SPACE_TYPE_NAME” - To display only space types on map as a label text. Example: DEFIBRILLATOR for id 7348</p>
  <p>“SPACE_CATEGORY_NAME” - To display only space categories on map as a label text. Example: SAFETY for id 7348</p>
  <p>“INTERNAL_ADDRESS” - To display only internal addresses on map as a label text. Example: 51/D for id 7348</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      loadTopologies()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Lets user load topologies for current session

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadTopologies ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      loadOptionalFeatures(optionalFeatureList: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Lets user load optional features for current session.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func loadOptionalFeatures ( optionalFeatureList : VenueService . VenueOptionalFeatureList )
  ```

  </pre>

  </div>

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
  <td><code> </code><em><code>optionalFeatureList</code></em><code> </code></td>
  <td><div>
  <p>The list of optional feature enum VenueOptionalFeature.</p>
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

