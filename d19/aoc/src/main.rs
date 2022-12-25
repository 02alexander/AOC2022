extern crate regex;

use std::io::BufRead;

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
struct State {
    minerals: [u32; 4],
    robots: [u32; 4],
    time_left: u32
}

impl State {
    pub fn new(start_time: u32) -> State {
        State {
            minerals: [0, 0, 0, 0],
            robots: [1, 0, 0, 0],
            time_left: start_time,
        }
    }

    pub fn can_buy(&self, drill: usize, blueprint: &[[u32; 4]; 4]) -> bool {
        for (mat, cost) in self.minerals.iter().zip(blueprint[drill]) {
            if cost > *mat {
                return false
            }
        }
        true
    }

    pub fn buy_drill(&mut self, drill: usize, blueprint: &[[u32; 4]; 4]) {

        for (mat, cost) in self.minerals.iter_mut().zip(blueprint[drill]) {
            *mat -= cost;
        }
        self.robots[drill] += 1;
    }
    pub fn step(&mut self) {
        for (mineral, nrobots) in self.minerals.iter_mut().zip(self.robots) {
            *mineral += nrobots;
        }
        self.time_left -= 1;
    }
}


fn search(mut state: State, blueprint: &[[u32; 4]; 4] ) -> u32{
    let mut bg = 0;

    
    if state.time_left < 1 {
        return state.minerals[3];
    }

    let mut max_needed: Vec<u32> = (0..4).map(|i| blueprint.iter().map(|itm| itm[i]).max().unwrap()).collect();
    max_needed[3] = 1000;
    //println!("{:?}", max_needed);

    'outer: for i in 0..4 {
        if state.robots[i] >= max_needed[i] {
            continue;
        }
        let mut cur_state = state.clone();
        while !cur_state.can_buy(i, &blueprint) {
            if cur_state.time_left <= 1 {
                cur_state.step();
                bg = bg.max(cur_state.minerals[3]);
                continue 'outer;
            }
            cur_state.step();
        }
        cur_state.step();
        cur_state.buy_drill(i, &blueprint);
        
        bg = bg.max(search(cur_state.clone(), blueprint));
    }

    while state.time_left >= 1 {
        state.step();
    }

    bg.max(state.minerals[3])
}

fn main() {
    let stdin = std::io::stdin().lock();
    let re = regex::Regex::new("(\\d+)").unwrap(); 


    let mut sm = 1;
    for (i, line) in stdin.lines().enumerate().take(3) {
        let line = line.unwrap();
        let vs: Vec<_> =  re.captures_iter(&line).map(|v| (&v[0]).parse::<u32>().unwrap()).collect();
        let mut blueprint = [[0;4];4];
        blueprint[0] = [vs[1], 0, 0, 0];
        blueprint[1] = [vs[2], 0, 0, 0];
        blueprint[2] = [vs[3], vs[4], 0, 0];
        blueprint[3] = [vs[5], 0, vs[6], 0];
  
        let res = search(State::new(32), &blueprint);
        println!("{:?}", res*(i as u32+1));
        //sm += res*(i as u32+1);
        sm *= res;
        //sm += res*(i as u32+1);
    }
    println!("{sm}");
}


