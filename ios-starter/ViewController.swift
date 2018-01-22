//
//  ViewController.swift
//  ios-starter
//
//  Created by Pulkit Arora on 17/01/18.
//  Copyright © 2018 Pulkit Arora. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
	@IBOutlet weak var label1: UILabel!
	@IBOutlet weak var label2: UILabel!
	
	override func viewDidLoad() {
		label1.text = L10n.helloWorld
		label2.text = L10n.helloWorld
	}
}
